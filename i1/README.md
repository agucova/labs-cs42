# Pseudointerrogación 1 - IIC1103

## Introducción

Este laboratorio es una adaptación de la primera interrogación que se hizo en el primer semestre de este año en el curso IIC1103, Introducción a la Programación.

La gracia de este formato es que puedo darles comentarios y pistas sobre los ejercicios, y adicionalmente puedo recibir su desarrollo y darles sugerencias o tips.

Si no sabes como correr programas en el entorno de laboratorio (CS50 Lab), deberías primero pasar por el [lab introductorio](https://lab.cs50.io/agucova/labs-cs42/master/hola/) y el [lab de la clase-2]((https://lab.cs50.io/agucova/labs-cs42/master/clase-2/)).

{% next "Seguir" %}

## Volleyball 1999

En el Volleyball actual, al equipo que gana una jugada se le suma un punto. Pero antes de 1999, la cosa era diferente: solo se sumaba un punto si el equipo que sacaba era el que ganaba la jugada. Es decir, los siguientes dos ejemplos muestran lo que podría pasar durante una jugada cuando le toca sacar al equipo A.

- El equipo A saca. El equipo A gana la jugada. Se le suma un punto al equipo A. Sigue sacando A.

- El equipo A está sacando. El equipo B gana la jugada. NO se le suma un punto al equipo B. Ahora saca B.

Es decir, si el equipo que está sacando gana la jugada, suma un punto y sigue sacando. En cambio si pierde la jugada, no suma puntos y le toca sacar al otro equipo.

El partido lo gana el primero en llegar a los **5 puntos**, pero con una condición: hay que ganar con al menos **dos puntos de diferencia**. Si un equipo llega a 5 puntos, pero el otro tiene 4, hay que seguir jugando hasta que uno de los dos equipos logre superar al otro por 2 puntos.

En esta pregunta se te pide un programa, `volleyball.py` que reciba qué equipo gana cada jugada y escriba el desarrollo del partido. Tu programa debe seguir las reglas del Volleyball de 1999.

## Input Format

Para cada jugada se te entregara un `str con el equipo que ha ganado esa jugada (A o B).

### Constraints

Siempre empieza sacando A.

El partido es a 5 puntos, pero hay que ganar por 2 puntos o más de diferencia, por lo que podrían los equipos terminar con más de 5 puntos.

## Output Format

Para indicar el inicio del partido, el programa debe imprimir EMPIEZA.

Para cada jugada, debes escribir quién saca (SACA A), quién gana (GANA B), y los puntos (siguiendo el formato de ejemplo A 3 B 1).

Para indicar el término del partido, el programa debe imprimir FINAL.

{% next "Ejemplos" %}

## Ejemplos

### Input

Ejecuta el programa:

```shell
$ python volleyball.py
```

Y entrega las jugadas en el terminal:

```
A
B
A
A
A
B
B
A
A
A
```

### Output

```
EMPIEZA
SACA A
GANA A
A 1 B 0
SACA A
GANA B
A 1 B 0
SACA B
GANA A
A 1 B 0
SACA A
GANA A
A 2 B 0
SACA A
GANA A
A 3 B 0
SACA A
GANA B
A 3 B 0
SACA B
GANA B
A 3 B 1
SACA B
GANA A
A 3 B 1
SACA A
GANA A
A 4 B 1
SACA A
GANA A
A 5 B 1
FINAL
```