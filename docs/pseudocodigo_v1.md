PSEUDOCOGIGO
# Pseudocódigo v1 – Import nostalgia: falta mucho para llegar a casa?

INICIO

 MOSTRAR "Mensaje de bienvenida"

REPETIR

MOSTRAR menu:
1. Calcular distancia entre dos lugares
2. Millas o Kilometros
3. Diferencia horaria
4. Destinos multiples
5. Todas las anteriores
6. Salir
LEER opcion

SI opcion == 1 ENTONCES
lugar1 = pedir_lugar()
lugar2 = pedir_lugar()
mostrar_distancia(lugar1, lugar2, unidad)

SINO SI opción == 2 ENTONCES
MOSTRAR "1. Kilometros  2. Millas"
LEER eleccion
SI eleccion == 1 ENTONCES
    unidad = "km"
SINO
unidad = "millas"
 FIN SI
 MOSTRAR "Unidad cambiada a ", unidad

SINO SI opción == 3 ENTONCES
lugar1 = pedir_lugar()
lugar2 = pedir_lugar()
mostrar_diferencia_horaria(lugar1, lugar2)
