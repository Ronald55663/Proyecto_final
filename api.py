import unicodedata  # Permite limpiar tildes/acentos de textos para compararlos sin errores
import requests # Librería externa para hacer peticiones HTTP (como pedir datos a una API)


"""
    Consulta la API Open-Meteo Geocoding para obtener 
    la latitud y longitud de una ciudad dada.
"""
url = "https://geocoding-api.open-meteo.com/v1/search"

def normalizar(texto):
    """
   Prepara un texto para compararlo: minúsculas, sin espacios
    extra y sin acentos.

    Ejemplo: ' México ' -> 'mexico'
    """
    # Quita espacios extra, pasa a minusculas y separa los acentos de las letras
    texto_sin_acentos = unicodedata.normalize("NFD", texto.strip().lower())
   # Deja solo las letras y borra los acentos
    return "".join(c for c in texto_sin_acentos if unicodedata.category(c) != "Mn") #!= "Mn" hace que se quede con todo lo que NO sea un acento suelta".

def obtener_coordenadas(ciudad, pais):
    """
    Busca una ciudad y su país en Open-Meteo.

    Retorna:
        dict: {"nombre": str, "pais": str, "lat": float, "lon": float}
        None: Si la ciudad no existe o no coincide con el país indicado.

    Lanza:
        ConnectionError: Si hay problemas de red, timeout o formato de respuesta inválido.
    """
    # Parámetros de consulta que se envían en la URL
    parametros = {
        "name": ciudad.strip(),  # Nombre de la ciudad sin espacios sobrantes
        "count": 10,             # Pedimos hasta 10 coincidencias para poder filtrar por país
        "language": "es",        # Solicita los nombres de países en español cuando sea posible
        "format": "json",        # Indica que queremos la respuesta en formato JSON
    }
    
# Bloque try/except para atrapar fallos de comunicación o respuestas rotas
    try:
        # Realiza la petición GET con un límite máximo de 10 segundos de espera
        respuesta = requests.get(url, params=parametros, timeout=10)
        # Si el servidor responde con un código de error HTTP (404, 500, etc.), lanza excepción
        respuesta.raise_for_status()
        # Convierte el cuerpo JSON de la respuesta en un diccionario de Python
        datos = respuesta.json()
    except requests.exceptions.Timeout:
        # Se dispara si el servidor tarda más de 10 segundos en responder
        # El from none oculta el detalle técnico original para que el error se vea limpio y claro
        raise ConnectionError("la API tardó demasiado en responder.") from None
    except requests.exceptions.RequestException:
        # Cubre falta de internet, fallo de DNS o problemas generales de conexión
        raise ConnectionError("no se pudo contactar la API (¿sin internet?).") from None
    except ValueError:
        # Se dispara si respuesta.json() falla porque no llegó un JSON válido
        raise ConnectionError("la API devolvió una respuesta inesperada.") from None

    # Extrae la lista "results"; si no existe en el JSON, devuelve una lista vacía []
    resultados = datos.get("results", [])

    # Normalizamos el país ingresado por el usuario para compararlo sin acentos ni mayúsculas
    pais_buscado = normalizar(pais)

    # Recorremos las ciudades devueltas por la API buscando la que coincida con el país
    for lugar in resultados:
        pais_api = normalizar(lugar.get("country", ""))
        if pais_api == pais_buscado:
            # Devolvemos un diccionario limpio solo con los campos que necesita el programa
            return {
                "nombre": lugar.get("name"),
                "pais": lugar.get("country"),
                "lat": lugar.get("latitude"),
                "lon": lugar.get("longitude"),
                "timezone": lugar.get("timezone"),
            }

    # Si no hubo resultados o ninguno coincidió con el país, devolvemos None
    return None


# Este bloque solo se ejecuta si corres "python api.py" directamente,
# NO cuando lo importas desde main.py
if __name__ == "__main__":
    import sys
    #Formato para que la terminal de Windows muestre correctamente los acentos y caracteres especiales
    sys.stdout.reconfigure(encoding="utf-8")


# Pruebas rápidas del módulo
print(obtener_coordenadas("Salt Lake City", "Estados Unidos"))
print(obtener_coordenadas("Barquisimeto", "Venezuela"))
print(obtener_coordenadas("Xyzabc", "Mexico"))  # Debe imprimir None