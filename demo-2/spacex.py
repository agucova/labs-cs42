criterios = []

criterios.append("1. No lanzar si el viento a los 162 pies de altura de la plataforma de lanzamiento excede los 30 nudos.")

criterios.append("2. No lanzar si las condiciones en alta alturas tienen un viento que pudiera a llevar a problemas de control para el vehículo de lanzamiento.")

criterios.append("3. No lanzar a través de una capa de nubes con grueso mayor a 4.500 pies, que se extienda a temperaturas de congelación.")

criterios.append("4. No lanzar dentro de 10 millas naúticas de cúmulos con superficies que se extiendan a temperaturas de congelación.")

criterios.append("5. No lanzar dentro de 10 millas naúticas del borde de una tormenta eléctrica que está produciendo rayos con un período menor a 30 minutos, según el último par de mediciones.")

criterios.append("6. No lanzar dentro de 10 millas naúticas de una nube yunque.")

criterios.append("7. No lanzar dentro de 5 millas naúticas de nubes alteradas que se extiendan a temperaturas de congelación (< 0ºC) y contengan precipitación moderada o mayor.")

criterios.append("8. No lanzar dentro de 3 millas naúticas de una tormenta eléctrica con nubes de escombro.")

criterios.append("9. No lanzar a través cúmulos formados por, o directamente conectados a, columnas de humo.")

criterios.append("10. Retrasar por 30 minutos si ha habido un rayo en un radio de 10 millas naúticas alrededor de la plataforma o la ruta de vuelo.")

criterios.append("11. Retrasar por 15 minutos si las lecturas de medidores de campo eléctrico dentro de 5 millas naúticas de la zona de lanzamiento exceden los +/- 1.500 V/m.")

def preguntar(criterio):
    while True:
        respuesta = input(criterio + " [si/no] ").lower().strip()
        if respuesta in ["si", "no"]:
            break
    return respuesta