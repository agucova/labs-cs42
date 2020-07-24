# Números Introescos

Bienvenido ✨ al tercero y muy original ejercicio de la I1 de IIC1103, *Números Introescos*.

## Introducción

Un número introesco es un número que contiene los dígitos 1, 1, 0 y 3 (en cualquier orden). Por ejemplo, son números introescos 1103, 1130, 222302211, 10101313, pero no son números introescos 103, ni 311, ni 123, ni 10101515 ni ningún número de 3 dígitos o menos. Nota en particular que el 103 no lo es dado que no tiene dos veces al número 1.

Para ayudarte, cuentas con la siguiente función ya implementada

```python
def introesco(x):
    # retorna True si x es un número introesco, False si no.
```

Además, vienen implementadas `digito(x,i)` y `largo(x)`, igual que en el ejercicio anterior.

Tu programa, `numeros_pythonescos.py` debe imprimir todos los números introescos en el rango que se te indique, y finalizar imprimiendo el número de números introescos que encontraste en dicho rango.

Por ejemplo, los números introescos entre 1100 y 1150 son:

```python
1103
1130
```

Al final, debes imprimir cuántos números introescos encontraste, por lo que se imprimiría, en el ejemplo anterior, además:
```python
2
```

Si no hay números introescos en algún rango, solo debes imprimir 0 (el número de números que encontraste).

{% next "Formato" %}

## Formato

### Input Format

Recibirás dos números enteros (*int*) `a`, `b`.

### Constraints

`a, b` son positivos enteros y se cumple que `a` ≤ `b.`

### Output Format

Debes imprimir como resultado todos los números introescos entre `a y b` (ambos incluidos). En la última línea, debes imprimir el número de números introescos que encontraste.

{% next "Mas Ejemplos" %}

## Mas Ejemplos

### Input

```python
1
10
```
### Output

```python
0
```
### Input

```python
1000
2000
```

### Output

```python
1013
1031
1103
1130
1301
1310
6
```

{% next "Envío y Tests" %}

### Envío y Tests

Debido a que `check50` es relativamente lento (puede tomar ~30 segundos), primero prueba la funcionalidad de tu programa tu mismo!

Para probar si tu programa funciona como debería, corre el siguiente comando en tu terminal, iniciando sesión con tu usuario y contraseña de GitHub si es que te lo solicita. Por razones de seguridad, verás asteriscos (`*`) en vez de los carácteres de tu contraseña.

```bash
check50 agucova/cs42/master/numeros-introescos
```

Si tu programa pasa las pruebas de `check50`, entonces ya puedes enviar tu problema para marcarlo como finalizado! Ejecuta el siguiente comando en el Terminal:

```bash
submit50 agucova/cs42/master/numeros-introescos
```

{% next "Siguiente ejercicio" %}

### Siguiente ejercicio

Felicitaciones 🎉! Estás a punto de terminar la I1.

Ahora que has terminado este ejercicio, puedes seguir con el [siguiente y último ejercicio de la I1](https://lab.cs50.io/agucova/labs-cs42/master/fronteras-de-wakanda/), *Fronteras de Wakanda*. **(Prepárate).**