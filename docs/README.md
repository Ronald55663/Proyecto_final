# ==========================================
#  Titulo: import nostalgia: ¿Falta mucho para llegar a casa? 
#  Integrantes: Ronald Medina y Christian Mendoza
# ==========================================

# Descripcion del funcionamiento del programa: 
Es un proyecto desarrollado en python que permite comparar distancia entre dos lugares significativas para el usuario. El programa buscara las coordenadas usando los datos geograficos reales desde una API para despues hacer los calculos necesarios. El usuario podra elegir si lo quiere en kilometros o millas, y por el momento el usuario podra ver la diferencia horaria y escoger destinos multiples. 

# Ejemplo de salida:
-Mensaje de bienvenida.
-Desarrollo
-Menu de opciones
	-El usuario escoge si quiere millas o kilometros
	-Si quiere ver la diferencia horaria.
	-Si quiere escoger destinos multiples.
	-O si quiere ver todas las anteriores

# Como instalar y ejecutar:
-Clonar el repositorio en VSC:https://github.com/Ronald55663/Proyecto_final.git
-Instalar tzdata desde la terminal (python -m pip install tzdata)

-Correr el programa “nostalgia.py”.

# Funcionamiento de la API:
El proyecto utiliza Open-Meteo Geocoding API para buscar iformacion geografica de las cuidades ingresadas por el usuario

La API permite obtener:

-Latitud.
-Longitud

# Creacion de funciones: 
Se crearon las funciones para guardar la informacion de el usuario 

# Extensiones
Agregamos dos funciones al programa: Diferencia horaria y Destinos multiples por que su grado de dificultad no era tan alto y
lo quisimos hacer simple pero que funcionara correcto y lo entendieramos por completo.

1. Diferencia horaria:
	- Compara la hora actual entre ciudades usando la zona horaria con el modulo zoneinfo.
	- Se puede utilizar desde el menu principal, escogiendo la opcion indicada.
	- Ejemplo de salida: 
	Hora local en Guadalajara : 20:00 (America/Mexico)
	Hora local en Barquisimeto : 22:00 (America/Venezuela) 
	Diferencia horaria: Barquisimeto está 2 hora por delante de Guadalajara.

2. Destinos multiples:
	- Permite ingresar varios destinos desde una misma ciudad de origen.
	- Se puede utilizar desde el menu principal, escogiendo la opcion indicada.
	- Ejemplo de salida:
	***Destinos desde (Ciudad origen) del mas cercano al mas lejano:
		- Guadalajara = 500 km. Viaje en avion: 3 h 0 m y viaje en carro 24 h 0 m
		- 0Barquisimeto = 1000 km. Viaje en avion: 6 h 0 m y viaje en carro 48 h 0 m

    (Las cantidades son solo ejemplos, no son cantidades reales)