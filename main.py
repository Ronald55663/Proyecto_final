"""
primero crear el mensaje de bienvenida con dos opciones

despues crear un if con opcion 1 y opcion 2
preguntar al usuario y despues imprimir lo ingresado

 """

import sys
from api import obtener_coordenadas

print("\n***MENSAJE DE BIENVENIDA***")
print("\nHola, bienvenido a nuestro proyecto final, titulado “ import nostalgia: ¿Falta mucho para llegar a casa?")
print("esperamos sea de tu agrado y dejes un tip si te gusto y si no, deja tu feedback para mejorar.") 
print("Gracias, vales mil nunca cambies.\n")

#Creamos la funcion para mostrar el menu de opciones
def mostrar_menu():
    print("\n***MENU DE OPCIONES***")
    print("1.Calcular la distancia entre dos ciudades")
    print("2. Salir")

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

#Creamos la funcion para pedir una ciudad al usuario
def pedir_ciudad(tipo):
    # Pedimos la ciudad al usuario hasta que ingrese una válida.
    # Usamos un bucle while para repetir la solicitud hasta que el usuario ingrese una ciudad válida.
    while True:
        # .strip() quita los espacios del principio y del final. Así, si el
        # usuario solo escribe espacios, el texto queda vacío y lo rechazamos.
        ciudad = input(f"Ciudad de origen o destino? {tipo}: ").strip()

        # Verificamos si el usuario escribió algo.
        # Si el usuario no escribió nada, le pedimos que vuelva a intentar.
        if ciudad:
            return ciudad
        else: 
            print("El campo no puede estar vacío. Por favor, inténtalo de nuevo.")

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