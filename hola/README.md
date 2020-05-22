# Holi uwu

## Introducción

Hola, mundo! A la derecha, en el *editor de texto*, está el programa mas simple que se puede hacer en Python, un "Hello, World".

Un programa de *Hello, World* es un programa computacional que se utiliza para demostrar la sintaxis (estructura) más básica de un lenguaje de programación determinado.

El programa solo tiene una tarea (aunque no una menor, computacionalmente): mostrar el mensaje *"Hola, mundo"* (o similares), a su usuario.

A pesar de que el código ya viene escrito en este caso (en un archivo llamado *hola.py*), tendremos que ejecutarlo, y para eso tendremos que aprender a usar un *terminal*.

{% next "Seguir" %}

## Terminales

![Un terminal en el juego Fallout](https://media.giphy.com/media/lptIayuGHV9Utu3iTv/giphy.gif)

Un *terminal* es esencialmente una interfaz de texto entre una persona y un computador, que permite al usuario indicar instrucciones que el computador debe seguir.

En un terminal, hay ciertas líneas de texto que permiten emitir instrucciones, llamadas comandos, es por esto que los terminales también reciben el nombre de *interfaz de línea de comandos*, en inglés *command line interface* (CLI).

Probablemente ya has visto terminales varias veces, suele ser típicos de películas como Terminator, La Matrix, y Hackers, al igual que incontables juegos de hacking.

Aunque es verdad que los hackers suelen utilizar terminales de forma frecuente, esta herramienta no está reservado a ellos, todo computador moderno viene con uno!

> En MacOS puedes encontrar una aplicación llamada Terminal, en Windows encontrarás a cmd.exe y a Powershell, y en Ubuntu está GNOME Terminal.

A pesar de eso, debido a que cada terminal funciona distinto (aunque casi todos poseen fuertes similitudes), utilizaremos un terminal remoto, que está corriendo en un computador en Estados Unidos desde el momento que abriste esta ventana.

En este caso, el terminal se encuentra abajo del *editor de texto*, y vamos a empezar aprendiendo unos cúantos comandos básicos.

{% next "Seguir" %}

## Listando archivos

Si apretas el botón de carpeta que está al margen del editor de texto, podrás ver los archivos que hay en tu entorno de programación en este momento. Apreta el botón de nuevo para ocultar el menú.

Si estás empezando desde cero, solo debería haber un archivo, *hola.py*, el programa que queremos ejecutar.

En la ventana de Terminal que está justo debajo del editor, deberías ver un signo de dólar ($). Este signo de dólar es llamado *prompt*, y corresponde a el "diálogo" que te permite escribir comandos. Para empezar, escribe lo siguiente precisamente en el terminal y después apreta *Enter*:

```bash
ls
```

Deberías ver solamente *hola.py*. Lo que acabas de hacer es nuevamente pedir una lista de archivos, solo que esta vez usando tu teclado a través de una CLI, en vez de usar botones en una interfaz gráfica (graphical user interface o GUI). Mas especificamente, lo que acabas de hacer es *ejecutar* un comando llamado `ls`, abreviación de *list*. (Es común este tipo de abreviaciones porque los informáticos son flojos y prefieren ahorrar teclas)

De ahora en adelante, *ejecutar* (o correr) un comando significa escribirlo en una ventana del terminal, y apretar *Enter*. Todos los comandos son case-sensitive, o sensible a las minúsculas o mayúsculas, por lo cual asegúrate de escribirlo tal como aparece!

{% next "Seguir" %}

## Ahora sí, lo prometo

Ahora que sabes ejecutar comandos, podemos por fin correr el programa de Hola, mundo. Para hacerlo ejecuta el siguiente comando en tu terminal:

```bash
python hola.py
```

Este comando básicamente le indica al  interpretador de Python, escrito `python` que debe ejecutar el archivo llamado `hola.py` y mostrarte su resultado.

Al correrlo, deberías ver que la pantalla del terminal dió un resultado a tu comando, **Hola, mundo!**.
