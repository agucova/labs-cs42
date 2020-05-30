# SpaceX Demo-2

## Contexto

![El Crew Dragon montado sobre el cohete Falcon 9](https://cdn.mos.cms.futurecdn.net/bFPyWsn99JYEAVESBqK3sn.jpg)

El martes pasado [estaba agendando](https://cnnespanol.cnn.com/video/nasa-space-lanzamiento-espacio-posponen-naves-estados-unidos-tripulacion-perspectivas-mexico-live-ana-mejia/) el primer lanzamiento de astronautas al espacio por parte de una compañía privada, SpaceX.

En una alianza con la NASA, se tenía planeado usar el Falcon 9, un cohete reutilizable de última generación, con tal de llevar el módulo tripulado Crew Dragon a la Estación Espacial Internacional (ISS).

{% video https://www.youtube.com/watch?v=sZlzYzyREAI %}

Un pobre ayudante de Desafíos decidió cubrir este lanzamiento en vivo, junto con otros grandes de la ingeniería aeroespacial.

Lamentablemente, debido a las condiciones climáticas cambiantes, el lanzamiento tuvo que ser pospuesto a solo minutos de su comienzo.

El nuevo lanzamiento está agendado para el sábado 22 (hoy, probablemente), pero los criterios climáticos mínimos son los mismos.

{% next "Seguir" %}


## Criterios de Compromiso al Lanzamiento

Antes de lanzar cualquier cohete (especialmente uno tripulado), es de suma importancia verificar que efectivamente se cumplen una serie de criterios mínimos, llamados los _Launch Commit Criteria_ (criterios de compromiso al lanzamiento, LLC), que se diferencian entre dos categorías:

- **Lighting Launch Commit Criteria (LLCC)**: Criterios que están diseñados para evitar golpes de rayos en vuelo. Pueden ser rayos naturales, aunque en su mayoría son atraídos por las cargas electromagnéticas alrededor del propulsor químico. Corresponden a un 40% de los delays en lanzamientos.

- **User Launch Commit Criteria (ULCC)**: Estos son criterios climáticos específicos para cada cohete, adaptados a su construcción y requerimientos. Incluyen vientos de bajo nivel para que no se caiga o incline el cohete y la visibilidad del cohete desde el suelo.

En Estados Unidos, el rol de evaluar continuamente que se cumplan estas condiciones recae en la [Ala Espacial Nº 45](https://en.wikipedia.org/wiki/45th_Space_Wing) de la Fuerza Área Estadounidense, quien libera [reportes](https://www.patrick.af.mil/Portals/14/Weather/Falcon%209%20Dragon%20Crew%20Demo-2%20L-1%20Day%20Forecast%20-%2030%20May%20Launch.pdf?ver=2020-05-29-092624-233) periódicos con un **POV** (Probability of Violation), la probabilidad de que no se cumpla una o mas de los criterios durante la ventana de lanzamiento.

{% next "Seguir" %}

## Falcon 9

En el caso específico del Falcon 9, todos los [criterios](https://www.nasa.gov/pdf/649911main_051612_falcon9_weather_criteria.pdf) [^1] son los siguientes:

1. **No lanzar** si el viento a los 162 pies de altura de la plataforma de lanzamiento excede los 30 nudos. (15.4 m/s)

2. **No lanzar** si las condiciones en alta alturas tienen un viento que pudiera a llevar a problemas de control para el vehículo de lanzamiento.

3. **No lanzar** a través de una capa de nubes con grueso mayor a 4.500 pies, que se extienda a temperaturas de congelación.

4. **No lanzar** dentro de 10 millas naúticas de cúmulos con superficies que se extiendan a temperaturas de congelación.

5. **No lanzar** dentro de 10 millas naúticas del borde de una tormenta eléctrica que está produciendo rayos con un período menor a 30 minutos, según el último par de mediciones.

6. **No lanzar** dentro de 10 millas naúticas de una [nube yunque](https://es.wikipedia.org/wiki/Cumulonimbus_incus).

7. **No lanzar** dentro de 5 millas naúticas de nubes alteradas que se extiendan a temperaturas de congelación (< 0ºC) y contengan precipitación moderada o mayor.

8. **No lanzar** dentro de 3 millas naúticas de una tormenta eléctrica con nubes de escombro.

9. **No lanzar** a través cúmulos formados por, o directamente conectados a, columnas de humo.

10. **Retrasar** por 30 minutos si ha habido un rayo en un radio de 10 millas naúticas alrededor de la plataforma o la ruta de vuelo.

11. **Retrasar** por 15 minutos si las lecturas de medidores de campo eléctrico ([_field mills_](https://en.wikipedia.org/wiki/Field_mill)) dentro de 5 millas naúticas de la zona de lanzamiento exceden los +/- 1.500 V/m.

[^1]: Los criterios fueron ligeramente simplificados, y se hizo caso omiso de los criterios de excepción.

{% next "Seguir" %}

## Especificación

Tu tarea es implementar un programa en Python que guíe a un LWO (Oficial del Clima de Lanzamiento) a verificar los criterios antes presentados, y determinar si proseguir, detener o retrasar un lanzamiento del Falcon 9.

A tu derecha vas a encontrar dos archivos ya creados, `criterios_f9.py` y `comprobar_criterios.py`. El primero contiene código ya escrito con cada criterio ya mencionado, y te permitirá acceder a la lista de criterios como una variable (`criterios[]`) dentro de `comprobar_criterios.py`.

## Uso

El programa deberá preguntarle al usuario por cada criterio en la lista, esperando una respuesta afirmativa (`si`) o negativa (`no`). Dependiendo de las respuestas del usuario, deberás devolver un veredicto para el lanzamiento.

```bash
$ python3 comprobar_criterios.py
1. No lanzar si el viento a los 162 pies de altura de la plataforma de lanzamiento excede los 30 nudos. [si/no] si
2. No lanzar si las condiciones en alta alturas tienen un viento que pudiera a llevar a problemas de control para el vehículo de lanzamiento. [si/no] si
...
Veredicto: retrasar.
```
{% next "Comprobar y Enviar" %}

### Envío

Debido a que `check50` es relativamente lento (puede tomar ~30 segundos), siempre prueba la funcionalidad de tu programa tu mismo primero!

Para probar si tu programa funciona como debería, corre el siguiente comando en tu terminal, iniciando sesión con tu usuario y contraseña de GitHub si es que te lo solicita. Por razones de seguridad, verás asteriscos (`*`) en vez de los carácteres de tu contraseña.

```bash
check50 agucova/cs42/master/demo-2
```

Si tu programa pasa las pruebas de `check50`, entonces ya puedes enviar tu problema para marcarlo como finalizado! Ejecuta el siguiente comando en el Terminal, tu usuario y contraseña deberían haberse quedado guardados de usos anteriores de `check50`y `submit50`.

```bash
submit50 agucova/cs42/master/demo-2
```
