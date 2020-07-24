# Fronteras de Wakanda

![uwu](https://nypost.com/wp-content/uploads/sites/2/2019/12/wakanda-usda.jpg?quality=90&strip=all&w=618&h=410&crop=1)

Holi! Sorprendentemente, si, **este es el título de esta sección**, y digo sección porque de hecho *Fronteras de Wakanda* son tres ejercicios en la I1, lo que significa que tendrás que enviar tres archivos distintos.

## Parte 1

El presidente de Wakanda está estudiando construir un muro en su frontera con Narnia, y quiere que los narnianos lo paguen.

Los muros se representan como strings de esta forma:

```
V--V----V--P--VV---V------V--P--V--V
```

Donde `V` indica que hay un Puesto de Vigilancia en ese lugar, `P` un Puesto de Paso, y `-` simplemente una reja. **Todos los muros siempre empiezan y terminan con un `V`**, y todos los muros **tienen al menos una reja.**

En este problema se te pide que escribas el programa `costo.py`, que recibe un str con el muro en el formato descrito más arriba, y retorna un *int* con el costo del tramo rejado más largo entre dos puestos (ya sea `V` o `P`). **Cada reja cuesta 10.**

En `V--V----V--P--VV---V------V--P--V--V` el tramo más largo son 6 rejas (entre la sexta `V` y la séptima `V`). Como cada reja cuesta 10, la función retorna 60.

En `V--P--V--P--V el tramo` más largo son 2 rejas (hay varios iguales: desde la primera `V` a la primera `P`, o desde la primera `P` a la segunda `V`, ...). Como cada reja cuesta 10, la función retorna 20.

{% next "Formato" %}

## Formato

### Input Format

Un *str* con el muro en el formato descrito.

### Constraints

El muro siempre empieza y termina con un V. Todos los muros tienen al menos una reja. Cada reja cuesta 10.

### Output Format

Un *int* con el costo del tramo rejado más largo.

{% next "Ejemplos" %}

## Ejemplos

### Input

```
V--V----V--P--VV---V------V--P--V--V
```

### Output

```python
60
```

### Input

```
V--P--V--P--V

```

### Output

```python
20
```

### Input

```
V-V

```

### Output

```python
10
```

### Input

```
V--P---P--V

```

### Output

```python
30
```

### Input

```
P-------------V-----------P

```
### Output

```python
130
```

{% next "Envío y Tests" %}

### Envío y Tests

Debido a que `check50` es relativamente lento (puede tomar ~30 segundos), primero prueba la funcionalidad de tu programa tu mismo!

Para probar si tu programa funciona como debería, corre el siguiente comando en tu terminal, iniciando sesión con tu usuario y contraseña de GitHub si es que te lo solicita. Por razones de seguridad, verás asteriscos (`*`) en vez de los carácteres de tu contraseña.

```bash
check50 agucova/cs42/master/fdw-costo
```

Si tu programa pasa las pruebas de `check50`, entonces ya puedes enviar tu problema para marcarlo como finalizado! Ejecuta el siguiente comando en el Terminal:

```bash
submit50 agucova/cs42/master/fdw-costo
```

{% next "Parte 2" %}