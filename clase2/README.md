# clase2

## Enviando desafíos

Ahora en adelante, cada clase va a estar acompañada de un conjunto de desafíos o *problem sets* (psets). La idea es que puedas resolver problemas propuestos en Python, y utilizar dos herramientas del curso, *check50* y *submit50*, para revisar y enviar tus psets, respectivamente.

Algunos problemas de este pset son adaptados de pruebas de IIC1103, Introducción a la Programación. La idea es que los problemas vayan creciendo en dificultad y no solo te permitan practicar lo pasado en cada clase, sino que te preparen para IIC1103.

Si no sabes como correr programas en el entorno de laboratorio (CS50 Lab), deberías primero pasar por el [lab introductorio](https://lab.cs50.io/agucova/labs-cs42/master/hola/).

{% next "Seguir" %}

## Sobre los problemas

Los problemas cuentan con tres partes:

- **Contexto: (a veces):** El contexto del problema, muchas veces explica conceptos previos para que entiendas el problema planteado. En un comparador de ADN, por ejemplo, podría ser la explicación de como funcionan los comparadores y toda la bioquímica y genética asociada.
- **Especificación:** Esto es el enunciado del problema, te dice lo que tu programa debería hacer.
- **Uso:** Esto te indica como tu programa debería ser utilizado. Por ejemplo, especifica en que forma el usuario va a interactuar con tu programa. Debes procurar que tu programa se ajuste perfectamente a esto ya que el evaluador de problemas es automatizado, y espera que cumplas con cada ejemplo.
- **Pistas (a veces):** Especialmente en problemas desafiantes, este apartado te dará algunas pistas sobre como poder solucionarlo.
- **Envío:** Esto te dice el comando que debes ejecutar para comprobar tu problema (puedes hacerlo ilimitadas veces) y para enviar tu problema a la plataforma de evaluación (donde se te asigna un porcentaje para tu solución).

{% next "Seguir" %}

## Tu primer problema

Tu primer problema es simple y aburrido.

### Especificación
En un archivo llamado `hola.py`, implementa un programa que imprima (muestre) la frase `Hola, mundo!` en la pantalla del usuario.

Para mostrar el mensaje, tu programa debe hacer uso de `print()`y debe entregar precisamente el mensaje propuesto.

### Uso

```bash
$ python hola.py
Hola, mundo!
```

**Nota:** Cuando se habla sobre un comando en el terminal, se suele anteponer un `$` para indicar que es efectivamente un comando. Las lineas que no empiecen por `$` corresponden al output de tu programa.

### Envío

Para probar si tu programa funciona como debería, corre el siguiente comando en tu terminal:
```bash
$ check50 agucova/cs42/master/hola
```
Execute the below, logging in with your GitHub username and password when prompted. For security, you’ll see asterisks (*) instead of the actual characters in your password.

Si tu programa pasa las pruebas de `check50`, entonces ya puedes enviar tu problema para marcarlo como finalizado! Ejecuta el siguiente comando en el Terminal, iniciando sesión con tu usuario y contraseña de GitHub cuando te lo solicite. Por razones de seguridad, verás asteriscos (`*`) en vez de los carácteres de tu contraseña.

```bash
$ submit50 agucova/cs42/master/hola
```