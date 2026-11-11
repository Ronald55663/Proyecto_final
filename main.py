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


print("\n***MENU DE OPCIONES***")
print("1. Quieres las distancias en kilometros o millas")
print("2. zona horaria de cada destino")
print("3. quieres calcular mas de dos destinos")
print("4. todas las opciones")
print("5. Salir")
opcion = input("Seleccione una opción: ")

if opcion == "1":
    nombre_ciudad = input("Ingrese el nombre de la primera ciudad: ")
    coordenadas = obtener_coordenadas(nombre_ciudad)
    nombre_ciudad_destino = input("Ingrese el nombre de la segunda ciudad: ")
    coordenadas_destino = obtener_coordenadas(nombre_ciudad_destino)
    if coordenadas and coordenadas_destino:
        print(f"Coordenadas de {coordenadas['nombre']}, {coordenadas['pais']}:")
        print(f"Latitud: {coordenadas['lat']}, Longitud: {coordenadas['lon']}")
        print(f"Coordenadas de {coordenadas_destino['nombre']}, {coordenadas_destino['pais']}:")
        print(f"Latitud: {coordenadas_destino['lat']}, Longitud: {coordenadas_destino['lon']}")

        
elif opcion == "5":
    print("Saliendo...")
    sys.exit()
else:
    print("Opción no válida.")