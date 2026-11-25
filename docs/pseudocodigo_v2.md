Import Nostalgia
Pseudocódigo – Versión 2
Programación orientada a objetos

1. Clase Ciudad (ciudad.py)

DEFINIR clase Ciudad:

ATRIBUTOS:
-nombre
-pais
-latitud
-longitud
-timezone

MÉTODO init(nombre, pais, latitud, longitud, timezone):

GUARDAR nombre en self.nombre
GUARDAR pais en self.pais
GUARDAR latitud en self.latitud
GUARDAR longitud en self.longitud
GUARDAR timezone en self.timezone

MÉTODO distancia_a(otra):

UTILIZAR calcular_distancia() de utils.py

ENVIAR:
    latitud de esta ciudad
    longitud de esta ciudad
    latitud de la otra ciudad
    longitud de la otra ciudad

DEVOLVER distancia en kilómetros

FIN MÉTODO


MÉTODO diferencia_horaria_con(otra):

OBTENER fecha y hora actual en UTC

CONVERTIR la hora actual a la zona horaria de esta ciudad

CONVERTIR la hora actual a la zona horaria de la otra ciudad

OBTENER la diferencia entre ambas zonas horarias

DEVOLVER diferencia en horas

SI ocurre un error con la zona horaria:

    DEVOLVER None

FIN MÉTODO

MÉTODO str():

DEVOLVER nombre, país y coordenadas de la ciudad

FIN MÉTODO

FIN CLASE Ciudad

2. Programa principal (main.py)

INICIO:

MOSTRAR mensaje de bienvenida

ESTABLECER unidad preferida = kilómetros

REPETIR:
MOSTRAR menú:

    1. Calcular distancia y tiempo entre dos ciudades
    2. Calcular diferencia horaria entre dos ciudades
    3. Calcular múltiples destinos desde un origen
    4. Cambiar unidad preferida
    5. Salir

SOLICITAR opción al usuario

SI opción = 1:

    SOLICITAR ciudad de origen
    VALIDAR que no esté vacía

    SOLICITAR país de origen
    VALIDAR que no esté vacío

    SOLICITAR ciudad de destino
    VALIDAR que no esté vacía

    SOLICITAR país de destino
    VALIDAR que no esté vacío

    CONSULTAR API Open-Meteo para obtener coordenadas

    SI ocurre un error de conexión:

        MOSTRAR mensaje de error
        REGRESAR al menú

    SI alguna ciudad no existe:

        MOSTRAR mensaje de ciudad no encontrada
        REGRESAR al menú

    CREAR objeto Ciudad para el origen
    CREAR objeto Ciudad para el destino

    INCLUIR las zonas horarias de ambas ciudades

    CALCULAR distancia:

        distancia_km = origen.distancia_a(destino)

    CONVERTIR kilómetros a millas

    CALCULAR tiempo estimado en avión

    CALCULAR tiempo estimado en automóvil

    FORMATEAR tiempos en horas y minutos

    MOSTRAR resumen del viaje:

        Ciudad de origen
        Ciudad de destino
        Distancia en kilómetros
        Distancia en millas
        Tiempo estimado en avión
        Tiempo estimado en automóvil

    ACLARAR que la distancia es en línea recta

SI opción = 2:

    SOLICITAR ciudad de origen
    SOLICITAR país de origen

    SOLICITAR ciudad de destino
    SOLICITAR país de destino

    CONSULTAR API Open-Meteo para obtener información
    de ambas ciudades, incluyendo sus zonas horarias

    SI ocurre un error de conexión:

        MOSTRAR mensaje de error
        REGRESAR al menú

    SI alguna ciudad no existe:

        MOSTRAR mensaje de ciudad no encontrada
        REGRESAR al menú

    CREAR objeto Ciudad para el origen
    CREAR objeto Ciudad para el destino

    CALCULAR diferencia horaria utilizando:

        origen.diferencia_horaria_con(destino)

    OBTENER la hora actual en UTC

    CONVERTIR la hora actual a la zona horaria
    de cada ciudad

    MOSTRAR:

        Ciudad de origen y su hora local
        Ciudad de destino y su hora local
        Diferencia horaria entre ambas ciudades

    INDICAR si la ciudad de destino está:

        Adelantada
        Atrasada
        En la misma hora

SI opción = 3:

    SOLICITAR ciudad de origen
    SOLICITAR país de origen

    CONSULTAR API Open-Meteo para obtener coordenadas

    SI ocurre un error de conexión:

        MOSTRAR mensaje de error
        REGRESAR al menú

    SI la ciudad no existe:

        MOSTRAR mensaje de ciudad no encontrada
        REGRESAR al menú

    CREAR objeto Ciudad de origen

    CREAR lista vacía para almacenar destinos

    REPETIR:

        SOLICITAR nombre de ciudad de destino

        SI el usuario escribe "listo":

            FINALIZAR ingreso de destinos

        SOLICITAR país del destino

        CONSULTAR API para obtener coordenadas

        SI ocurre un error de conexión:

            MOSTRAR mensaje de error
            CONTINUAR con el siguiente destino

        SI la ciudad no existe:

            MOSTRAR mensaje de ciudad no encontrada
            CONTINUAR con el siguiente destino

        CREAR objeto Ciudad de destino

        CALCULAR distancia desde el origen:

            distancia_km = origen.distancia_a(destino)

        GUARDAR ciudad de destino y distancia
        en la lista de destinos

    HASTA que el usuario escriba "listo"

    SI no existen destinos válidos:

        MOSTRAR mensaje indicando que no hay destinos

    SI existen destinos:

        ORDENAR destinos de menor a mayor distancia

        UTILIZAR sorted() y lambda

        MOSTRAR destinos ordenados

        PARA cada destino:

            MOSTRAR nombre de ciudad
            MOSTRAR distancia
            MOSTRAR distancia en la unidad preferida
            CALCULAR tiempo estimado en avión
            CALCULAR tiempo estimado en automóvil
            MOSTRAR tiempos formateados

SI opción = 4:

    SOLICITAR unidad preferida

    VALIDAR que sea kilómetros o millas

    ACTUALIZAR unidad preferida

SI opción = 5:

    MOSTRAR mensaje de despedida

    FINALIZAR programa

SI la opción no es válida:

    MOSTRAR mensaje de opción incorrecta

HASTA que el usuario decida salir

FIN

3. Módulo de utilidades y cálculos (utils.py)

IMPORTAR biblioteca matemática (math)

DEFINIR velocidades promedio:

velocidad_avion = 950 km/h
velocidad_auto = 100 km/h

DEFINIR factor de conversión:
km_x_millas = 0.621371
FUNCIÓN calcular_distancia(lat1, lon1, lat2, lon2):

RECIBIR coordenadas geográficas de dos ciudades

CONVERTIR latitudes y longitudes de grados a radianes

ESTABLECER radio de la Tierra = 6371 km

CALCULAR diferencia entre latitudes

CALCULAR diferencia entre longitudes

APLICAR fórmula de Haversine

CALCULAR distancia en kilómetros

DEVOLVER distancia_km

FIN FUNCIÓN 
FUNCIÓN km_a_millas(distancia_km):
MULTIPLICAR distancia_km por km_x_millas
DEVOLVER resultado en millas

FIN FUNCIÓN


FUNCIÓN calcular_tiempo_viaje(distancia_km, velocidad):

DIVIDIR distancia_km entre velocidad

DEVOLVER tiempo en horas decimales

FIN FUNCIÓN


FUNCIÓN formatear_tiempo(horas):
MULTIPLICAR horas por 60

REDONDEAR resultado a minutos enteros

DIVIDIR minutos totales entre 60

OBTENER horas completas y minutos restantes

DEVOLVER tiempo en formato "X h YY min"

FIN FUNCIÓN


SI utils.py se ejecuta directamente:
CALCULAR distancia de prueba entre Madrid y París

MOSTRAR distancia en kilómetros

CALCULAR tiempo estimado en avión

CALCULAR tiempo estimado en automóvil

FORMATEAR tiempos en horas y minutos

MOSTRAR resultados
FIN SI
FIN

4. Módulo de consulta de ciudades (api.py)

INICIO
IMPORTAR biblioteca unicodedata
IMPORTAR biblioteca requests

DEFINIR URL de Open-Meteo Geocoding API


FUNCIÓN normalizar(texto):
ELIMINAR espacios sobrantes

CONVERTIR texto a minúsculas

SEPARAR caracteres de sus acentos

ELIMINAR los acentos

DEVOLVER texto normalizado

FIN FUNCIÓN


FUNCIÓN obtener_coordenadas(ciudad, pais):
PREPARAR parámetros de consulta:

    nombre de ciudad
    cantidad de resultados = 10
    idioma = español
    formato = JSON

INTENTAR:

    REALIZAR petición GET a Open-Meteo

    ESTABLECER tiempo máximo de espera = 10 segundos

    VERIFICAR respuesta del servidor

    CONVERTIR respuesta JSON a datos de Python

SI ocurre un error de tiempo de espera:

    LANZAR ConnectionError

    INFORMAR que la API tardó demasiado en responder

SI ocurre un error de conexión:

    LANZAR ConnectionError

    INFORMAR que no se pudo contactar con la API

SI la respuesta JSON es inválida:

    LANZAR ConnectionError

    INFORMAR que la API devolvió una respuesta inesperada

OBTENER lista de resultados de la API

NORMALIZAR país ingresado por el usuario

PARA cada lugar encontrado por la API:

    NORMALIZAR país devuelto por la API

    SI el país encontrado coincide con el país solicitado:

        CREAR diccionario con:

            nombre de ciudad
            país
            latitud
            longitud
            zona horaria (timezone)

        DEVOLVER diccionario

SI no se encuentra una ciudad que coincida:

    DEVOLVER None
FIN FUNCIÓN


SI api.py se ejecuta directamente:
CONFIGURAR codificación UTF-8

REALIZAR pruebas de búsqueda:

    Salt Lake City, Estados Unidos
    Barquisimeto, Venezuela
    Xyzabc, México

MOSTRAR resultados


FIN SI
