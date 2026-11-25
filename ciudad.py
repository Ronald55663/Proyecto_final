"""Agrupa los datos de una ubicación geográfica y las acciones relacionadas
con ella (como calcular la distancia hacia otra Ciudad o representarla en texto).
"""
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from utils import calcular_distancia

#Creamos la clase de una ciudad con sus coordenadas geográficas.
class Ciudad:
    

    def __init__(self, nombre, pais, latitud, longitud, timezone="UTC"):
        """
        Inicializa una instancia de Ciudad.
        
        Parámetros:
         nombre (str): nombre de la ciudad.
         pais (str): nombre del país.
         latitud (float): latitud geográfica en grados decimales.
         longitud (float): longitud geográfica en grados decimales.
         timezone (str): zona horaria de la ciudad
"""
        # Guardamos cada dato como atributo del objeto
        self.nombre = nombre
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud
        self.timezone = (
            timezone.strip()
            if isinstance(timezone, str) and timezone.strip()
            else "UTC"
        )
                            

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

    def diferencia_horaria_con(self, otra):
        """
        Calcula la diferencia horaria actual en horas entre esta ciudad y otra
        usando zoneinfo y la hora actual (respetando horario de verano)."""

        try:
            # Partimos de UTC y convertimos a cada zona en el instante actual
            # para que el horario de verano (DST) se refleje automáticamente.
            ahora_utc = datetime.now(ZoneInfo("UTC"))
            offset_propio = ahora_utc.astimezone(ZoneInfo(self.timezone)).utcoffset()
            offset_otra = ahora_utc.astimezone(ZoneInfo(otra.timezone)).utcoffset()

            if offset_propio is None or offset_otra is None:
                return None

            return (offset_otra - offset_propio).total_seconds() / 3600
        except ZoneInfoNotFoundError as error:
         # Evita que una zona horaria desconocida rompa el programa
         print(f"Detalle de zona horaria: {error}")
         return None

    def __str__(self):
        """Devuelve un texto legible con nombre, país y coordenadas."""
        # Formato con 2 decimales como en el ejemplo del Paso 7
        return f"{self.nombre}, {self.pais} ({self.latitud:.2f}, {self.longitud:.2f})"


if __name__ == "__main__":
    # Prueba rápida para comprobar que la clase funciona tal como se espera
    origen = Ciudad("San Marcos", "Guatemala", 14.9667, -91.7944, "America/Guatemala")
    destino = Ciudad("Salt Lake City", "Estados Unidos", 40.7608, -111.8910, "America/Denver")
    print(origen)
    print(f"{origen.distancia_a(destino):.2f} km")
    print(f"Diferencia horaria: {origen.diferencia_horaria_con(destino)} horas")

    
    