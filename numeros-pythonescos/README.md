# Números Pythonescos 🐍

Bienvenido al segundo ejercicio de la I1 de IIC1103!

Si no sabes como correr programas en el entorno de laboratorio (CS50 Lab), deberías primero pasar por el [lab introductorio](https://lab.cs50.io/agucova/labs-cs42/master/hola/) y el [lab de la clase-2]((https://lab.cs50.io/agucova/labs-cs42/master/clase-2/)).

## Introducción

Un número pythonesco es un número entero, positivo, que cumple con la siguiente propiedad:

**Si sumamos los cuadrados de cada uno de sus dígitos y seguimos el proceso con los resultados obtenidos hasta llegar a un número de un solo dígito, el resultado es 1 o 7.**

- 23 es pythonesco porque si sumamos los cuadrados de los dígitos que lo componen (2 y 3), nos da: 2² + 3² = 13, y repitiendo el proceso para 13, 1² + 3² = 10, y repitiendo el proceso para 10, 1² + 0² = 1.

- 89, en cambio, NO es pythonesco, ya que 8² + 9² = 145, 1² + 4² + 5² = 42, 4² + 2² = 20, 2² + 0² = 4, y 4 es un número de un solo digito que no es 1 ni 7.

- 7 es el único número de un dígito (además de 1) que es pythonesco ya que 7² = 49, 4² + 9² = 97, 9² + 7² = 130, 1² + 3² + 0² = 10 y 1² + 0² = 1.

Pueden existir números *pythonescos* de cualquier número de dígitos. Por ejemplo, son números pythonescos los siguientes: 91, 230, 1587 (y muchos otros, por supuesto).

Para este problema, cuentas con dos funciones ya implementadas que *DEBES USAR* y *NO PUEDES MODIFICAR:*

- `digito(x,i)`: recibe un *int* `x` y un *int* `i`, y retorna un *int* con el iésimo dígito de `x` (numerados desde 0). Por ejemplo, si `x` es 1896, `digito(x,0)` retorna 1, `digito(x,1)` retorna 8, `digito(x,2)` retorna 9 y `digito(x,3)` retorna 6. Para cualquier otro valor de `i` (que no sea válido), retorna -1.

- `largo(x)`: recibe un *int* `x`, retorna el número de dígitos que tiene. Por ejemplo, si `x` es 1896, `largo(x)` retorna 4.

Tu misión es escribir una función `pythonesco(x)` que reciba un *int* x y retorne un *bool* indicando si `x` es pythonesco o no (`True` si lo es, `False` si no lo es).

{% next "Formato" %}

## Formato

### Input Format

El número a comprobar si es pythonesco.

### Constraints

El número siempre será positivo y mayor o igual a 1.

### Output Format

`True` si el número es pythonesco, y `False` si no.

{% next "Ejemplos" %}

## Ejemplos

Corriendo tu programa con:
```shell
$ python numeros_pythonescos.py
```

### Input

```
5
```

### Output

```
False
```

### Input

```
1
```
### Output

```
True
```

### Input

```
131
```
### Output

```
False
```

### Input

```
163
```
### Output

```
True
```

{% next "Envío y Tests" %}

### Envío y Tests

Debido a que `check50` es relativamente lento (puede tomar ~30 segundos), primero prueba la funcionalidad de tu programa tu mismo!

Para probar si tu programa funciona como debería, corre el siguiente comando en tu terminal, iniciando sesión con tu usuario y contraseña de GitHub si es que te lo solicita. Por razones de seguridad, verás asteriscos (`*`) en vez de los carácteres de tu contraseña.

```bash
check50 agucova/cs42/master/numeros-pythonescos
```

Si tu programa pasa las pruebas de `check50`, entonces ya puedes enviar tu problema para marcarlo como finalizado! Ejecuta el siguiente comando en el Terminal:

```bash
submit50 agucova/cs42/master/numeros-pythonescos
```

{% next "Siguiente ejercicio" %}

### Siguiente ejercicio

Bien! Ahora que has terminado este ejercicio, puedes seguir con el [siguiente ejercicio de la I1](https://lab.cs50.io/agucova/labs-cs42/master/numeros-introescos/), *Números Introescos*. (Si, lo sé, la originalidad es notable acá).