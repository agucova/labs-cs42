# Fronteras de Wakanda

![uwu](https://nypost.com/wp-content/uploads/sites/2/2019/12/wakanda-usda.jpg?quality=90&strip=all&w=618&h=410&crop=1)

Holi! Sorprendentemente, si, **este es el título de esta sección**, y digo sección porque de hecho *Fronteras de Wakanda* son tres ejercicios en la I1, lo que significa que tendrás que enviar tres archivos distintos. (No te preocupes, no es taaaan terrible.)

Así que pon el lo-fi (o tu música preferida) y a programar 👩‍💻.

{% next "Parte 1" %}

## Parte 1

El presidente de Wakanda está estudiando construir un muro en su frontera con Narnia, y quiere que los narnianos lo paguen.

Los muros se representan como strings de esta forma:

```
V--V----V--P--VV---V------V--P--V--V
```

Donde `V` indica que hay un Puesto de Vigilancia en ese lugar, `P` un Puesto de Paso, y `-` simplemente una reja. **Todos los muros siempre empiezan y terminan con un `V`**, y todos los muros **tienen al menos una reja.**

En este problema se te pide que escribas el programa `costear.py`, que recibe un str con el muro en el formato descrito más arriba, y retorna un *int* con el costo del tramo rejado más largo entre dos puestos (ya sea `V` o `P`). **Cada reja cuesta 10.**

En `V--V----V--P--VV---V------V--P--V--V` el tramo más largo son 6 rejas (entre la sexta `V` y la séptima `V`). Como cada reja cuesta 10, la función retorna 60.

En `V--P--V--P--V el tramo` más largo son 2 rejas (hay varios iguales: desde la primera `V` a la primera `P`, o desde la primera `P` a la segunda `V`, ...). Como cada reja cuesta 10, la función retorna 20.

{% next "Formato" %}

### Formato

#### Input Format

Una linea con el muro en el formato descrito.

#### Constraints

El muro siempre empieza y termina con un V. Todos los muros tienen al menos una reja. Cada reja cuesta 10.

#### Output Format

Un *int* con el costo del tramo rejado más largo.

{% next "Ejemplos" %}

### Ejemplos

#### Input 0

```
V--V----V--P--VV---V------V--P--V--V
```

#### Output 0

```python
60
```

#### Input 1

```
V--P--V--P--V
```

#### Output 1

```python
20
```

#### Input 2

```
V-V
```

#### Output 2

```python
10
```

#### Input 3

```
V--P---P--V
```

#### Output 4

```python
30
```

#### Input 5

```
P-------------V-----------P
```
#### Output 5

```python
130
```

{% next "Envío y Tests" %}

### Envío y Tests

Debido a que `check50` es relativamente lento (puede tomar ~30 segundos), primero prueba la funcionalidad de tu programa tu mismo!

Para probar si tu programa funciona como debería, corre el siguiente comando en tu terminal, iniciando sesión con tu usuario y contraseña de GitHub si es que te lo solicita. Por razones de seguridad, verás asteriscos (`*`) en vez de los carácteres de tu contraseña.

```bash
check50 agucova/cs42/master/fdw-costear
```

Si tu programa pasa las pruebas de `check50`, entonces ya puedes enviar tu problema para marcarlo como finalizado! Ejecuta el siguiente comando en el Terminal:

```bash
submit50 agucova/cs42/master/fdw-costear
```

{% next "Parte 2" %}

## Parte 2

En esta parte se te pide que implementes un programa `sepuede.py` que dado un *str* m con un muro, y un *int* i con una posición en el muro; y retorna un *bool* diciendo si se podría poner un Puesto de Paso en esa posición. Un Puesto de Paso se puede poner en una posición `i` si la posición tiene una reja, así como la posición de antes y la de después. Las posiciones están numeradas desde el 0 hasta el `len(m) - 1`. La i dada siempre estará entre 0 y `len(m) - 1`.

Por ejemplo, para la reja V--V----V--P--VV---V------V--P--V--V, la función retornaría lo siguiente:

`True` en la posición 5, porque es una reja así como la posición de antes y después.
`False` en la posición 3, porque es una `V`
`False` en la posición 4, porque hay una V en la posición de antes.
`False` en la posición 2, porque es una V en la posición de después.
Recuerda que los muros se representan como strings de esta forma:

```
V--V----V--P--VV---V------V--P--V--V

```

Donde V indica que hay un Puesto de Vigilancia en ese lugar, P un Puesto de Paso, y - simplemente una reja. Todos los muros siempre empiezan y terminan con una V, y todos los muros tienen al menos una reja.

{% next "Formato" %}


### Formato

#### Input Format

Una liena (que llamaremos `m`) con un muro en el formato descrito, y otra línea (que llamaremos `i`) con una posición en el muro.

#### Constraints

El muro siempre empieza y termina con un `V`.
Todos los muros tienen al menos una reja.
La posición dada siempre estará entre `0` y `len(muro) - 1`.

### Output Format

Un bool si se puede poner P en esa posición (`True`) o si no se puede (`False`).

{% next "Ejemplos" %}

### Ejemplos

#### Input 0

```
V--V----V--P--VV---V------V--P--V--V
5
```

#### Output 0

```
True
```

#### Input 1

```
V--V----V--P--VV---V------V--P--V--V
3
```

#### Output 1

```
False
```

#### Input 2

```
V--V----V--P--VV---V------V--P--V--V
4

```
#### Output 2

```
False
```

#### Input 3

```
V--V----V--P--VV---V------V--P--V--V
2
```

#### Output 3

```
False
```

{% next "Envío y Tests" %}

### Envío y Tests

Debido a que `check50` es relativamente lento (puede tomar ~30 segundos), primero prueba la funcionalidad de tu programa tu mismo!

Para probar si tu programa funciona como debería, corre el siguiente comando en tu terminal, iniciando sesión con tu usuario y contraseña si es que te lo pide.

```bash
check50 agucova/cs42/master/fdw-sepuede
```

Si tu programa pasa las pruebas de `check50`, entonces ya puedes enviar tu problema para marcarlo como finalizado! Ejecuta el siguiente comando en el Terminal:

```bash
submit50 agucova/cs42/master/fdw-sepuede
```

{% next "Parte 3" %}

## Parte 3

Un punto ciego de longitud `k`, es un tramo de muro de longitud `k` sin ningún Puesto de Vigilancia (solo Puestos de Paso o reja).

De esa forma, en `V--V----V--P--VV---V------V--P--V--V` hay 4 puntos ciegos de longitud 5:

- `V--V----VxxxxxVV---V------V--P--V--V`,
- `V--V----V--P--VV---Vxxxxx-V--P--V--V`,
- `V--V----V--P--VV---V-xxxxxV--P--V--V`,
- `V--V----V--P--VV---V------VxxxxxV--V`
-
En cambio, en `V--V----V--P--VV---V------V--P--V--V` hay solo 1 punto ciego de longitud 6:
- `V--V----V--P--VV---VxxxxxxV--P--V--V`

En `V--V----V--P--VV---V------V--P--V--V` hay 0 puntos ciegos de longitud 7.

En esta parte se te pide que implementes el programa `ciegos.py` que dado un *str* `m` con un muro y un *int* `k` con una longitud, retorna un *int* con el número de puntos ciegos de longitud `k` que tiene el muro. La k dada siempre estará entre `0` y `len(m) - 1`.

### Formato

#### Input

Una linea con un muro (`m`) en el formato descrito y otra línea con la longitud (`k`) para los puntos ciegos.

#### Constraints

El muro siempre empieza y termina con un V.
Todos los muros tienen al menos una reja.
k siempre entre 0 y len(m) - 1.

#### Output

Una linea con el número de puntos ciegos de longitud `k` que tiene el muro.

{% next "Ejemplos" %}

### Ejemplos

#### Input 0

```
V--V----V--P--VV---V------V--P--V--V
5
```

#### Output 0

```python
4
```

#### Input 1

```
V--V----V--P--VV---V------V--P--V--V
6
```

#### Output 1

```python
1
```

#### Input 2

```
V--V----V--P--VV---V------V--P--V--V
7
```

#### Output 2

```python
0
```

#### Input 3

```
V--V----V--P--VV---V-----V--P--V--V
5
```

#### Output 3

```python
3
```

{% next "Envío y Tests" %}

### Envío y Tests

Debido a que `check50` es relativamente lento (puede tomar ~30 segundos), primero prueba la funcionalidad de tu programa tu mismo!

Para probar si tu programa funciona como debería, corre el siguiente comando en tu terminal, iniciando sesión con tu usuario y contraseña si es que te lo pide.

```bash
check50 agucova/cs42/master/fdw-ciegos
```

Si tu programa pasa las pruebas de `check50`, entonces ya puedes enviar tu problema para marcarlo como finalizado! Ejecuta el siguiente comando en el Terminal:

```bash
submit50 agucova/cs42/master/fdw-ciegos
```

{% next "El fin" %}

# The end

Si llegaste hasta aquí y tus checks pasaron, felicitaciones ✨!

La I1 no era fácil, especialmente si recién estás empezando a entender Python, así que descansa (o ándate a mimir) y siéntete orgulloso 🎉.

{% video https://www.youtube.com/watch?v=9nfwvbT2sl8 %}