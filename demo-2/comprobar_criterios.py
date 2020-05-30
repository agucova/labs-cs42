# Esto importa lo escrito en el archivo spacex.py a este archivo
# Esto trae dos cosas, spacex.criterios, una lista con cada criterio, y spacex.preguntar, una función para preguntarle a un usuario sobre un criterio.
import spacex

# EJEMPLO

# Esto le pregunta a el usuario si cumple o no el primer criterio, devolviendo "si" o "no".
# Si responde algo mas, lo vuelve a preguntar.
respuesta = spacex.preguntar(spacex.criterios[0])

# Muestra la respuesta del usuario
print(respuesta)