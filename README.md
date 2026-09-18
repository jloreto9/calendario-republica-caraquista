# Calendario República Caraquista

Calendario de la temporada LVBP 2026/2027 de **Leones del Caracas**, publicado como archivo `.ics` para suscripción directa en Google Calendar, Apple Calendar y Outlook (vía `webcal://`).

## Suscribirse al calendario

URL raw del `.ics`:

```
https://raw.githubusercontent.com/jloreto9/calendario-republica-caraquista/main/calendario/calendario_republica_caraquista.ics
```

URL `webcal://` (recomendada para suscripción — se actualiza sola cuando el archivo cambia en este repo):

```
webcal://raw.githubusercontent.com/jloreto9/calendario-republica-caraquista/main/calendario/calendario_republica_caraquista.ics
```

- **Google Calendar:** "Otros calendarios" → "+" → "Desde URL" → pegar la URL webcal (o https).
- **Apple Calendar:** Archivo → "Nueva suscripción de calendario…" → pegar la URL webcal.
- **Outlook:** Agregar calendario → "Suscribirse desde la web" → pegar la URL webcal (o https).

Nota: GitHub cachea `raw.githubusercontent.com` unos minutos tras cada push. Si actualizas el calendario y tu app no refleja el cambio de inmediato, espera unos minutos — es caché, no un problema de la suscripción.

## Estructura del repositorio

```
calendario/
  calendario_republica_caraquista.ics   ← archivo publicado, el que se consume vía webcal
generar_calendario_leones.py            ← script generador
README.md
```

## Cómo regenerar el calendario

El archivo `.ics` se genera con `generar_calendario_leones.py` a partir de la lista `JUEGOS` (fecha, rival, condición LOCAL/VISITA, hora, transmisión).

1. Editar `generar_calendario_leones.py`:
   - Agregar horas confirmadas en el diccionario `horarios_conocidos` (formato `"YYYY-MM-DD": "HH:MM"`).
   - Agregar transmisiones confirmadas en `transmisiones_conocidas` (formato `"YYYY-MM-DD": "Nombre del canal"`).
2. Ejecutar el script:

   ```bash
   python generar_calendario_leones.py
   ```

   Esto regenera `calendario_republica_caraquista.ics` en la raíz de la carpeta local.
3. Copiar el archivo regenerado a `/calendario` y publicar el cambio:

   ```bash
   cp calendario_republica_caraquista.ics calendario/calendario_republica_caraquista.ics
   git add calendario/calendario_republica_caraquista.ics
   git commit -m "Actualiza calendario con horas/transmisiones"
   git push
   ```

Los eventos usan un `UID` determinístico (hash de fecha + rival + condición), no aleatorio. Esto es intencional: permite que Google Calendar y demás apps **actualicen** el evento existente (por ejemplo, al agregarle hora o transmisión) en vez de duplicarlo cuando se vuelve a publicar el calendario.

## Convenciones de datos

- `LOCAL` = Leones juega en el Estadio Monumental Simón Bolívar (Caracas).
- `VISITA` = Leones juega en el estadio del rival.
- Mientras no haya hora confirmada, el evento se publica como evento de día completo con el título prefijado `[HORA PENDIENTE]`.
- Mientras no haya transmisión confirmada, la descripción del evento indica `Transmisión: Por confirmar`.
