# ==========================================
# PROYECTO FINAL : import nostalgia: ¿Falta mucho para llegar a casa?
# Ronald Medina y Christian Mendoza  
# ==========================================

import sys
from datetime import datetime
from zoneinfo import ZoneInfo
sys.stdout.reconfigure(encoding='utf-8')
from api import obtener_coordenadas
from ciudad import Ciudad
from utils import (
    calcular_tiempo_viaje,
    formatear_tiempo,
    km_a_millas,
    velocidad_auto,
    velocidad_avion,
)


print("\n***MENSAJE DE BIENVENIDA***")
print("\nHola, bienvenido a nuestro proyecto final, titulado “ import nostalgia: ¿Falta mucho para llegar a casa?")
print("esperamos sea de tu agrado y dejes un tip si te gusto y si no, deja tu feedback para mejorar.") 
print("Gracias, vales mil nunca cambies.\n")

#Creamos la funcion para mostrar el menu de opciones
def mostrar_menu(unidad_actual):
    print("\n***MENU DE OPCIONES***")
    print("1. Calcular la distancia y tiempo entre dos ciudades")
    print("2. Calcular diferencia horaria entre dos ciudades")
    print("3. Calcular múltiples destinos desde un origen")
    print(f"4. Cambiar unidad preferida (actual: {unidad_actual})")
    print("5. Salir")

#Creamos la funcion para pedir y guardar la unidad que el usuario escogio y asegurarnos que escribio algo valido.
def pedir_unidad():
    #Creamos un bucle while para que se repita hasta que el usuario ingrese una opcion valida
    while True:
        unidad = input("Que unidad quieres usar? (km/millas): ").strip().lower() #.strip para quitar espacios y .lower para pasar a minusculas.
        #Se crea un if para validar que la unidad ingresada sea valida y si no lo es, le pide al usuario que vuelva a intentar
        if unidad in ["km", "kilómetros", "kilometros"]:
            return "Kilometros"
        elif unidad in  ["millas", "mi"]:
            return "millas"
        else:
            print("Unidad no válida. Por favor, ingrese 'km' o 'millas'.")

# Creamos la funcion para pedir una ciudad al usuario y asegurarnos que escriba algo valido y no este vacio
def pedir_ciudad(tipo):
    # Pedimos la ciudad al usuario hasta que ingrese una válida.
    # Usamos un bucle while para repetir la solicitud hasta que el usuario ingrese una ciudad válida.
    while True:
        # .strip() quita los espacios del principio y del final. Así, si el
        # usuario solo escribe espacios, el texto queda vacío y lo rechazamos.
        ciudad = input(f"Ciudad de {tipo}: ").strip()

        # Verificamos si el usuario escribió algo.
        # Si el usuario no escribió nada, le pedimos que vuelva a intentar.
        if ciudad:
            return ciudad
        else:
            print("El campo no puede estar vacío. Por favor, inténtalo de nuevo.")

# Creamos la funcion para pedir un pais al usuario y asegurarnos que escriba algo valido y no este vacio
def pedir_pais(tipo):
    """Pide el país del origen o destino y evita entradas vacías."""
    while True:
        pais = input(f"País de {tipo}: ").strip()
        if pais:
            return pais
        else:
            print("El campo no puede estar vacío. Por favor, inténtalo de nuevo.")
"""
# creamos la funcion para buscar un lugar utilizando la API
def buscar_lugar(ciudad, tipo):
    # Si la ciudad no se encuentra, se le pide al usuario que ingrese otra.
    # iniciamos un bucle para buscar la ciudad hasta que obtengamos un resultado valido
    while True:
        lugar = obtener_coordenadas(ciudad)
    # Si lugar no es None, la búsqueda funcionó y lo devolvemos.
        if lugar:
            return lugar
        else:
            print(f"Escribe otra ciudad para el {tipo}.")
        ciudad = pedir_ciudad(tipo) 
"""
#Creamos la funcion que muestra el resumen estructurado del viaje con ambas unidades y tiempos
def mostrar_resumen(origen, destino, distancia_km, unidad_preferida):
    
    distancia_mi = km_a_millas(distancia_km)

    # Calculamos tiempos en horas decimales y los pasamos a formato "X h YY min"
    horas_avion = calcular_tiempo_viaje(distancia_km, velocidad_avion)
    horas_auto = calcular_tiempo_viaje(distancia_km, velocidad_auto)
    tiempo_avion_txt = formatear_tiempo(horas_avion)
    tiempo_auto_txt = formatear_tiempo(horas_auto)

    # Mostramos primero la unidad preferida del usuario y también la equivalencia
    if unidad_preferida == "millas":
        texto_distancia = f"{distancia_mi:,.2f} millas  ({distancia_km:,.2f} km)"
    else:
        texto_distancia = f"{distancia_km:,.2f} km  ({distancia_mi:,.2f} millas)"

    print("\n========== RESUMEN DEL VIAJE ==========")
    print(f"Origen:   {origen.nombre}, {origen.pais} " f"({origen.latitud:.4f}, {origen.longitud:.4f})")
    print(f"Destino:  {destino.nombre}, {destino.pais} " f"({destino.latitud:.4f}, {destino.longitud:.4f})\n")
    print(f"Distancia en línea recta: {texto_distancia}\n")
    print(f"Tiempo estimado en avión ({int(velocidad_avion)} km/h):  {tiempo_avion_txt}")
    print(f"Tiempo estimado en auto  ({int(velocidad_auto)} km/h):   {tiempo_auto_txt}\n")
    print("- La distancia es una aproximación en línea recta.")
    print("=======================================")

# Creamos la función para pedir datos, consultar la API, calcular y mostrar resultados
def calcular_viaje(unidad_preferida):
    """Gestiona la entrada de origen/destino, consulta la API y muestra el resumen."""
    # Pedimos origen y destino (ciudad y país) validando que no estén vacíos
    ciudad_origen = pedir_ciudad("origen")
    pais_origen = pedir_pais("origen")

    ciudad_destino = pedir_ciudad("destino")
    pais_destino = pedir_pais("destino")

    print("\nConsultando datos...")

    # Consultamos la API separando errores de red (ConnectionError)
    # de ubicaciones no encontradas (datos is None). Si falla, regresamos al menú.
    try:
        datos_origen = obtener_coordenadas(ciudad_origen, pais_origen)
        if datos_origen is None:
            print("Ciudad no encontrada")
            return

        datos_destino = obtener_coordenadas(ciudad_destino, pais_destino)
        if datos_destino is None:
            print("Ciudad no encontrada")
            return
    except ConnectionError as error:
        print(f"Error de red: {error}")
        return

    # Creamos un objeto Ciudad para origen y otro para destino a partir de la API
    origen = Ciudad(
        datos_origen["nombre"],
        datos_origen["pais"],
        datos_origen["lat"],
        datos_origen["lon"],
        datos_origen.get("timezone", "UTC"),
    )
    destino = Ciudad(
        datos_destino["nombre"],
        datos_destino["pais"],
        datos_destino["lat"],
        datos_destino["lon"],
        datos_destino.get("timezone", "UTC"),
    )

    # Verificamos si origen y destino tienen exactamente las mismas coordenadas
    mismo_lugar = (
        origen.latitud == destino.latitud
        and origen.longitud == destino.longitud
    )

    if mismo_lugar:
        print("\nAviso: El origen y el destino son iguales (distancia de 0.00 km).")
        distancia_km = 0.0
    else:
        # Usamos el metodo distancia_a() de la clase Ciudad en vez de llamar directo a utils
        distancia_km = origen.distancia_a(destino)

    mostrar_resumen(origen, destino, distancia_km, unidad_preferida)

#Esta funcion es para consultar ciudades y mostrar la diferencia horaria.
def extension_diferencia_horaria():
    ciudad_origen = pedir_ciudad("origen")
    pais_origen = pedir_pais("origen")
    ciudad_destino = pedir_ciudad("destino")
    pais_destino = pedir_pais("destino")

    print("\nConsultando zonas horarias...")

    try:
        datos_origen = obtener_coordenadas(ciudad_origen, pais_origen)
        if datos_origen is None:
            print(f"Ciudad no encontrada: '{ciudad_origen}, {pais_origen}'.")
            return

        datos_destino = obtener_coordenadas(ciudad_destino, pais_destino)
        if datos_destino is None:
            print(f"Ciudad no encontrada: '{ciudad_destino}, {pais_destino}'.")
            return
    except ConnectionError as error:
        print(f"Error de red al consultar zonas horarias: {error}")
        return

    origen = Ciudad(
        datos_origen["nombre"],
        datos_origen["pais"],
        datos_origen["lat"],
        datos_origen["lon"],
        datos_origen.get("timezone", "UTC"),
    )
    destino = Ciudad(
        datos_destino["nombre"],
        datos_destino["pais"],
        datos_destino["lat"],
        datos_destino["lon"],
        datos_destino.get("timezone", "UTC"),
    )

    diferencia = origen.diferencia_horaria_con(destino)
    if diferencia is None:
        print("No se pudo calcular la diferencia horaria para las zonas indicadas.")
        return

    # Hora local actual en ambas ciudades
    ahora_utc = datetime.now(ZoneInfo("UTC"))
    try:
        hora_origen = ahora_utc.astimezone(ZoneInfo(origen.timezone)).strftime("%H:%M") 
        hora_destino = ahora_utc.astimezone(ZoneInfo(destino.timezone)).strftime("%H:%M")
        print(f"\nHora local en {origen.nombre}:  {hora_origen} ({origen.timezone})")
        print(f"Hora local en {destino.nombre}: {hora_destino} ({destino.timezone})")

        #.strftime("%H:%M"): convierte la fecha y hora en un texto con el formato que queremos
        # %H representa las horas en formato de 24 horas y %M representa los minutos
    
    except Exception:
        pass

    horas_abs = abs(diferencia)
    texto_horas = "1 hora" if horas_abs == 1 else f"{horas_abs:g} horas"

    # abs() representa las horas en valor absoluto, quitando el signo negativo del numero
    # y despues con el if mostramos un mensaje diferente si es menor, mayor o igual a la zona horaria origen

    if diferencia > 0:
        print(f"Diferencia horaria: {destino.nombre} está {texto_horas} por delante de {origen.nombre}.")
    elif diferencia < 0:
        print(f"Diferencia horaria: {destino.nombre} está {texto_horas} por detrás de {origen.nombre}.")
    else:
        print(f"Diferencia horaria: {destino.nombre} tiene la misma hora que {origen.nombre}.")

#Con esta funcion creamos un bucle para que el usuario ingrese destinos hasta que escriba "listo"
# y ordenamos los resultados del mas cercano al mas lejano
def extension_destinos_multiples(unidad_actual):

    # Pedimos y validamos primero la ciudad de origen
    ciudad_origen = pedir_ciudad("origen")
    pais_origen = pedir_pais("origen")

    print("\nConsultando ciudad de origen...")
    try:
        datos_origen = obtener_coordenadas(ciudad_origen, pais_origen)
        if datos_origen is None:
            print(f"No se encontró la ciudad de origen: '{ciudad_origen}, {pais_origen}'.")
            return
    except ConnectionError as error:
        print(f"Error de red al consultar el origen: {error}")
        return

    origen = Ciudad(
        datos_origen["nombre"],
        datos_origen["pais"],
        datos_origen["lat"],
        datos_origen["lon"],
        datos_origen.get("timezone", "UTC"),
    )

    destinos_calculados = []
    print("\nIngresa destinos uno por uno. Escribe 'listo' en la ciudad para terminar.")

    # Bucle hasta que el usuario escriba 'listo'
    while True:
        entrada_destino = input("\nCiudad de destino (o escribe 'listo' para finalizar): ").strip()
        if not entrada_destino:
            print("La ciudad de destino no puede estar vacía.")
            continue

        # Condición de salida del bucle (insensible a mayúsculas y espacios)
        if entrada_destino.lower() == "listo":
            break

        pais_destino = pedir_pais("destino")

        try:
            datos_destino = obtener_coordenadas(entrada_destino, pais_destino)
            if datos_destino is None:
                print(f"Destino omitido: no se encontró '{entrada_destino}, {pais_destino}'.")
                continue

            destino = Ciudad(
                datos_destino["nombre"],
                datos_destino["pais"],
                datos_destino["lat"],
                datos_destino["lon"],
                datos_destino.get("timezone", "UTC"),
            )

            distancia_km = origen.distancia_a(destino)
            destinos_calculados.append((destino, distancia_km))
            print(f"Agregado: {destino.nombre}, {destino.pais} ({distancia_km:.2f} km).")
        except ConnectionError as error:
            # Si falla la red en un destino puntual, avisamos y seguimos con los demás
            print(f"Destino omitido por error de red en '{entrada_destino}': {error}")
            continue

    if not destinos_calculados:
        print("\nNo se agregaron destinos válidos para calcular.")
        return

    # Ordenamos de menor a mayor distancia usando sorted() y una función lambda
    # Investigamos sobre la funcion de key=lambda, la cual sirve para crear una pequeña funcion en una sola linea,
    # recibe un elemento llamado item y devuelve el elemento en posicion 1.
    #  
    destinos_ordenados = sorted(destinos_calculados, key=lambda item: item[1])

    print(f"\n=== DESTINOS DESDE {origen.nombre.upper()} (MÁS CERCANO A MÁS LEJANO) ===")
    for indice, (destino, distancia_km) in enumerate(destinos_ordenados, start=1):
        if unidad_actual.lower() in ("mi", "millas", "miles"):
            texto_distancia = f"{km_a_millas(distancia_km):.2f} millas"
        else:
            texto_distancia = f"{distancia_km:.2f} km"

        t_avion = formatear_tiempo(calcular_tiempo_viaje(distancia_km, velocidad_avion))
        t_auto = formatear_tiempo(calcular_tiempo_viaje(distancia_km, velocidad_auto))
        print(f"{indice}. {destino.nombre}, {destino.pais} -> {texto_distancia} | Avión: {t_avion} | Auto: {t_auto}")

def main():
    
    # la bienvenida se imprime una sola vez al inicio del programa.
    print("*** Calculadora de Distancias ***")

# Unidad por defecto del proyecto (en kilómetros)
    unidad_preferida = "km"

    # Bucle principal del menú hasta que el usuario elija salir
    while True:
        mostrar_menu(unidad_preferida)
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            try:
                calcular_viaje(unidad_preferida)
            except Exception as error:
                # Red de seguridad para evitar que un error inesperado cierre el programa
                print(f"Ocurrió un error inesperado: {error}")
        elif opcion == "2":
            try:
                extension_diferencia_horaria()
            except Exception as error:
                print(f"Ocurrió un error inesperado en diferencia horaria: {error}")
        elif opcion == "3":
            try:
                extension_destinos_multiples(unidad_preferida)
            except Exception as error:
                print(f"Ocurrió un error inesperado en destinos múltiples: {error}")
        elif opcion == "4":
            unidad_preferida = pedir_unidad()
            print(f"Unidad actualizada a: {unidad_preferida}")
        elif opcion == "5":
            print("¡Gracias por usar nuestro programa! ¡Esperamos sea de tu agrado!")
            break
        else:
            print("Opción inválida. Por favor, elige 1, 2, 3, 4 o 5.")

# Esta línea hace que main() se ejecute solo cuando corremos este archivo
# directamente (python main.py), y no cuando otro archivo lo importa.
if __name__ == "__main__":
    main()