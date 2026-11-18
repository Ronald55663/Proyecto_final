import math

#Creamos la funcion para calcular la distancia de dos ciudades usando la formula de Haversine
def calcular_distancia(lat1=40.4168, lon1=-3.7038, lat2=48.8566, lon2=2.3522):
    # Convertimos las coordenadas de grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Radio de la Tierra en kilómetros
    radio_tierra_km = 6371.0

    dis_lat = lat2_rad - lat1_rad #Distancia entre latitudes
    dis_lon = lon2_rad - lon1_rad #Distancia entre longitudes

    # Fórmula de Haversine
    a = math.sin(dis_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dis_lon / 2)**2

    distancia_km = 2 * radio_tierra_km * math.asin(math.sqrt(a))

    #Guardamos el resultado con el return
    return distancia_km

#Mandamos llamar la funcion calcular_distancia e imprimimos el resultado con 2 decimales
resultado = calcular_distancia()
print(f"{resultado:.2f} km.")