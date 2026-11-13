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
-Correr el programa “nostalgia.py”.

# Funcionamiento de la API:
El proyecto utiliza Open-Meteo Geocoding API para buscar iformacion geografica de las cuidades ingresadas por el usuario

La API permite obtener:

-Nombre de la ciudad.
-Pais.
-Latitud.
-Longitud
-Zona horaria. 

La imformacion recibida se procesa P