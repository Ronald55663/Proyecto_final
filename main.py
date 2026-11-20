# ==========================================
# PROYECTO FINAL : import nostalgia: ¿Falta mucho para llegar a casa?
# Ronald Medina y Christian Mendoza  
# ==========================================

import sys
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
    print(f"2. Cambiar unidad preferida (actual: {unidad_actual})")
    print("3. Salir")

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
    print(f"Origen:   {origen['nombre']}, {origen['pais']}" f"({origen['lat']:.4f}, {origen['lon']:.4f})")
    print(f"Destino:  {destino['nombre']}, {destino['pais']}" f"({destino['lat']:.4f}, {destino['lon']:.4f})\n")
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
    )
    destino = Ciudad(
        datos_destino["nombre"],
        datos_destino["pais"],
        datos_destino["lat"],
        datos_destino["lon"],
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
            unidad_preferida = pedir_unidad()
            print(f"Unidad actualizada a: {unidad_preferida}")
        elif opcion == "3":
            print("¡Gracias por usar nuestro programa! ¡Esperamos sea de tu agrado!")
            break
        else:
            print("Opción inválida. Por favor, elige 1, 2 o 3.")

# Esta línea hace que main() se ejecute solo cuando corremos este archivo
# directamente (python main.py), y no cuando otro archivo lo importa.
if __name__ == "__main__":
    main()