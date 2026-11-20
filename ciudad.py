"""Agrupa los datos de una ubicación geográfica y las acciones relacionadas
con ella (como calcular la distancia hacia otra Ciudad o representarla en texto).
"""

from utils import calcular_distancia

#Creamos la clase de una ciudad con sus coordenadas geográficas.
class Ciudad:
    

    def __init__(self, nombre, pais, latitud, longitud):
        """
        Inicializa una instancia de Ciudad.
        
        Parámetros:
         nombre (str): nombre de la ciudad.
         pais (str): nombre del país.
         latitud (float): latitud geográfica en grados decimales.
         longitud (float): longitud geográfica en grados decimales.
"""
        # Guardamos cada dato como atributo del objeto
        self.nombre = nombre
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud

    def distancia_a(self, otra):
        """
        Calcula la distancia en línea recta (en kilómetros) desde esta ciudad
        hasta otra instancia de Ciudad, reutilizando calcular_distancia de utils.py.
        """
# Utilizamos la función de utils.py para calcular la distancia
# y evitar repetir la fórmula de Haversine.

        return calcular_distancia(
            self.latitud,
            self.longitud,
            otra.latitud,
            otra.longitud,
        )

    def __str__(self):
        """Devuelve un texto legible con nombre, país y coordenadas."""
        # Formato con 2 decimales como en el ejemplo del Paso 7
        return f"{self.nombre}, {self.pais} ({self.latitud:.2f}, {self.longitud:.2f})"


if __name__ == "__main__":
    # Prueba rápida para comprobar que la clase funciona tal como se espera
    origen = Ciudad("San Marcos", "Guatemala", 14.9667, -91.7944)
    destino = Ciudad("Salt Lake City", "Estados Unidos", 40.7608, -111.8910)
    print(origen)
    print(f"{origen.distancia_a(destino):.2f} km")
