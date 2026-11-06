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

        SINO SI opción == 4 ENTONCES
                origen = pedir_lugar()
                LEER cantidad de destinos
                REPETIR cantidad VECES
                    destino = pedir_lugar()
                    mostrar_distancia(origen, destino, unidad)
                FIN REPETIR

        SINO SI opción == 5 ENTONCES
                lugar1 = pedir_lugar()
                lugar2 = pedir_lugar()
                mostrar_distancia(lugar1, lugar2, unidad)
                mostrar_diferencia_horaria(lugar1, lugar2)
                LEER cantidad de destinos extra
                REPETIR cantidad VECES
                    destino = pedir_lugar()
                    mostrar_distancia(lugar1, destino, unidad)
                FIN REPETIR

        SINO SI opción == 6 ENTONCES
                MOSTRAR "Hasta luego"

        SINO
                MOSTRAR "Opción no válida"
        FIN SI

    HASTA QUE opción == 6
FIN


FUNCION pedir_lugar()
    REPETIR
        LEER nombre (Ciudad, País)
        datos = buscar en la API(nombre)
        SI datos no existe ENTONCES
            MOSTRAR "Lugar no encontrado, intenta de nuevo"
        FIN SI
    HASTA QUE datos exista
    RETORNAR datos
FIN FUNCION

FUNCION mostrar_distancia(lugar1, lugar2, unidad)
    distancia = calcular distancia
    SI unidad == "millas" ENTONCES
        distancia = distancia * 0.621371
    FIN SI
    MOSTRAR "Distancia entre ", lugar1, " y ", lugar2, ": ", distancia, " ", unidad
FIN FUNCION

FUNCION mostrar_diferencia_horaria(lugar1, lugar2)
    hora1 = hora actual según zona horaria de lugar1
    hora2 = hora actual según zona horaria de lugar2
    diferencia = hora2 - hora1 (en horas)
    MOSTRAR "Diferencia horaria: ", diferencia, " horas"
FIN FUNCION
