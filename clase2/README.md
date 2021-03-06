# clase2

## Enviando desafíos

Ahora en adelante, cada clase va a estar acompañada de un conjunto de desafíos o *problem sets* (psets). La idea es que puedas resolver problemas propuestos en Python, y utilizar dos herramientas del curso, `check50` y `submit50`, para revisar y enviar tus psets, respectivamente.

Algunos problemas de este pset son adaptados de pruebas de IIC1103, Introducción a la Programación. La idea es que los problemas vayan creciendo en dificultad y no solo te permitan practicar lo pasado en cada clase, sino que te preparen para IIC1103.

Si no sabes como correr programas en el entorno de laboratorio (CS50 Lab), deberías primero pasar por el [lab introductorio](https://lab.cs50.io/agucova/labs-cs42/master/hola/).

**Nota:** `check50`y `submit50` fueron escritas en inglés, pero si quieres cambiar su lenguaje a español, ejecuta lo siguiente en terminal:
```bash
LANGUAGE=es
```

{% next "Seguir" %}

## Sobre los problemas

Los problemas cuentan con tres partes:

- **Contexto: (a veces):** Muchas veces explica conceptos previos para que entiendas el problema planteado. En un comparador de ADN, por ejemplo, podría ser la explicación de como funcionan los comparadores y toda la bioquímica y genética asociada.
- **Especificación:** El enunciado del problema, te dice lo que tu programa debería hacer.
- **Uso:** Esto te indica como tu programa debería ser utilizado. Por ejemplo, especifica en que forma el usuario va a interactuar con tu programa. Debes procurar que tu programa se ajuste perfectamente a esto ya que el evaluador de problemas es automatizado, y espera que cumplas con cada ejemplo.
- **Pistas (a veces):** Especialmente en problemas desafiantes, este apartado te dará algunas pistas sobre como poder solucionarlo.
- **Envío:** Esto te dice el comando que debes ejecutar para comprobar tu problema (puedes hacerlo ilimitadas veces) y para enviar tu problema a la plataforma de evaluación (donde se te asigna un porcentaje para tu solución, también puedes enviarlo cuantas veces quieras).

{% next "Seguir" %}

## Registrarse en el curso
Para poder usar `check50`y `submit50` es necesario que:

- Estés registrado en [github.com](https://github.com/) con tu mail UC.
- Asocies tu cuenta de GitHub con la página de `submit50`del curso. Para hacerlo, ingresa a [este link](https://submit.cs50.io/invites/0392889eaf614534906d60e45912e7db).

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

**Nota:** Cuando se habla sobre un comando en el terminal, cuando es conveniente, se antepone un `$` para indicar que es efectivamente un comando. Las lineas que no empiecen por `$` corresponden al output de tu programa. A veces se omite el `$` cuando el comando no debería tener output, o la idea es que tu lo averigues.

### Envío

Para probar si tu programa funciona como debería, corre el siguiente comando en tu terminal, iniciando sesión con tu usuario y contraseña de GitHub cuando te lo solicite. Por razones de seguridad, verás asteriscos (`*`) en vez de los carácteres de tu contraseña.

```bash
check50 agucova/cs42/master/hola
```

Si tu programa pasa las pruebas de `check50`, entonces ya puedes enviar tu problema para marcarlo como finalizado! Ejecuta el siguiente comando en el Terminal (si ya iniciaste sesión, no debería pedírtelo):

```bash
submit50 agucova/cs42/master/hola
```

{% next "Seguir" %}

## Revisando mi porcentaje

Con tal de facilitar el seguimiento en el curso, cuando usas `submit50` tu código se envía a [submit.cs50.io](https://submit.cs50.io), donde puedes ver el resultado de la evaluación de tu programa, junto con su porcentaje asociado.

Pruébalo ahora! Entra [aquí](https://submit.cs50.io/courses/190/) y ve si aparece el programa que envíaste. Si no aparece, comprueba si usaste `submit50` correctamente.

Ahora vamos a hacer problemas mas interesantes.

{% next "Seguir" %}

## Hipotenusa

### Especificación

Implementa un programa en un archivo nuevo, `hipotenusa.py` que reciba dos números enteros correspondientes a los catetos de un triángulo rectángulo, y devuelva la hipotenusa correspondiente, acorde con el [teorema de Pitágoras](https://es.wikipedia.org/wiki/Teorema_de_Pit%C3%A1goras).

Toma en cuenta que tu programa debe hacer uso de `print()`para mostrar el resultado y tu resultado debe mostrar la hipotenusa como un número entero, no un decimal. (Puedes asumir que la respuesta es entera).

### Uso

```bash
$ python hipotenusa.py
Primer cateto: 3
Segundo cateto: 4
Hipotenusa: 5
```

**Nota:** Aquí las dos primeras líneas son prompts de Python, mientras que la última es un output que utiliza `print()`. Puedes asumir que ambos catetos son números enteros (integers).

## Pistas

{% spoiler "Ver primera pista" %}
Aunque puedes hacer uso de funciones como `sqrt()` (raíz cuadrada) que deben ser importadas de la librería `math`, no es necesario, dado que tienes el poderoso operador `**`.
{% endspoiler %}

{% spoiler "Ver segunda pista" %}
Para pedir el primer cateto al usuario, tienes que usar `int(input("Primer cateto: "))`.
{% endspoiler %}

{% spoiler "Ver tercera pista" %}
Para poder mostrar la respuesta, necesitas mezclar un string, `"Hipotenusa: "`, con un número entero. Si intentas sumar ambos valores (concatenar), vas a obtener un error (porque no puedes sumar strings con enteros). La forma correcta es:
```python
print("Hipotenusa:", hipotenusa)
```

Donde `hipotenusa` es la variable (opcional) que contiene el entero con tu hipotenusa. La `","` hace que `print()` convierta automáticamente el entero a la derecha a un string, de forma que se pueda mostrar correctamente.

Adicionalmente, la coma añade un espacio entre ambas expresiones, así que ten cuidado con que tu output tenga dos espacios!

De forma alternativa (e igual de correcta), puedes convertir el entero a string, utilizando la función `str()`, y así poder usar la suma normalmente:

```python
print("Hipotenusa: " + str(hipotenusa))
```

{% endspoiler %}

### Envío

Debido a que `check50` es relativamente lento (puede tomar ~30 segundos), siempre prueba la funcionalidad de tu programa tu mismo primero!

Para probar si tu programa funciona como debería, corre el siguiente comando en tu terminal, iniciando sesión con tu usuario y contraseña de GitHub si es que te lo solicita. Por razones de seguridad, verás asteriscos (`*`) en vez de los carácteres de tu contraseña.

```bash
check50 agucova/cs42/master/hipotenusa
```

Si tu programa pasa las pruebas de `check50`, entonces ya puedes enviar tu problema para marcarlo como finalizado! Ejecuta el siguiente comando en el Terminal, tu usuario y contraseña deberían haberse quedado guardados de usos anteriores de `check50`y `submit50`.

```bash
submit50 agucova/cs42/master/hipotenusa
```

{% next "Final" %}

## Final

Felicitaciones! Hiciste el primer ejercicio completo de principio a fin. Si quieres seguir con los labs, puedes seguir con el [ejercicio demo-2](https://lab.cs50.io/agucova/labs-cs42/master/demo-2/), el siguiente lab.
