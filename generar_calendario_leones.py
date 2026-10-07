"""
Calendario República Caraquista
Generador de calendario .ics para Leones del Caracas - Temporada LVBP 2026/2027
Autor: script generado para Tigrin

Convención confirmada por Tigrin:
    DORADO = LOCAL   (Leones juega en el Estadio Monumental Simón Bolívar)
    BLANCO = VISITA  (Leones juega en el estadio del rival)

NOTA SOBRE DIRECCIONES: Venezuela no maneja direcciones postales
estructuradas (calle + numero) para estadios deportivos. Las
"direcciones" usadas abajo son la ubicacion/sector oficial documentado
(el mismo dato que usan Google Maps/Waze para geolocalizar cada
recinto), verificadas via busqueda web. No inventes un formato de
direccion tipo "Av. X, #123" porque no existe para estos estadios.
"""

from datetime import datetime, timedelta
import hashlib

# =========================================================
# 1. DATOS DEL CALENDARIO
# =========================================================
# Formato: (fecha "YYYY-MM-DD", rival, "LOCAL" o "VISITA", hora_HHMM o None, transmision o None)
#
# transmision: canal/plataforma de TV o streaming (ej. "Meridiano TV", "DirecTV").
# Se deja en None por ahora; se llenará más adelante con actualizar_transmisiones().
#
# Todos los rivales y condiciones (local/visita) fueron verificados
# contra las imágenes originales y confirmados por Tigrin.

JUEGOS = [
    # ---------------- OCTUBRE 2026 ----------------
    ("2026-10-13", "Águilas del Zulia",         "VISITA", "19:00", "ByM Sport, BeisbolPlay"),
    ("2026-10-14", "Águilas del Zulia",         "VISITA", "19:00", "ByM Sport, BeisbolPlay"),
    ("2026-10-15", "Bravos de Margarita",       "LOCAL",  "19:00", "1Baseball, BeisbolPlay"),
    ("2026-10-16", "Bravos de Margarita",       "LOCAL",  "19:00", "ByM Sport, BeisbolPlay"),
    ("2026-10-17", "Caribes de Anzoátegui",     "VISITA", "18:00", "Televen, BeisbolPlay"),
    ("2026-10-18", "Caribes de Anzoátegui",     "VISITA", "16:00", "Televen, BeisbolPlay"),
    ("2026-10-20", "Tiburones de La Guaira",    "VISITA", "19:00", "IVC, BeisbolPlay"),
    ("2026-10-23", "Tigres de Aragua",          "VISITA", "19:00", "ByM Sport, BeisbolPlay"),
    ("2026-10-24", "Navegantes del Magallanes", "LOCAL",  "20:00", "1Baseball, Meridiano TV, BeisbolPlay"),
    ("2026-10-25", "Navegantes del Magallanes", "VISITA", "19:00", "ByM Sport, Venevisión, BeisbolPlay"),
    ("2026-10-26", "Tigres de Aragua",          "LOCAL",  "19:00", "1Baseball, LVBP YouTube, BeisbolPlay"),
    ("2026-10-28", "Tiburones de La Guaira",    "LOCAL",  "19:00", "ByM Sport, BeisbolPlay"),
    ("2026-10-29", "Bravos de Margarita",       "VISITA", "19:00", "1Baseball, BeisbolPlay"),
    ("2026-10-30", "Bravos de Margarita",       "VISITA", "19:00", "1Baseball, Meridiano TV, BeisbolPlay"),
    ("2026-10-31", "Caribes de Anzoátegui",     "LOCAL",  "16:00", "ByM Sport, BeisbolPlay"),

    # ---------------- NOVIEMBRE 2026 ----------------
    ("2026-11-01", "Caribes de Anzoátegui",     "LOCAL",  "16:00", "Televen, BeisbolPlay"),
    ("2026-11-03", "Tiburones de La Guaira",    "LOCAL",  "19:00", "ByM Sport, BeisbolPlay"),
    ("2026-11-04", "Tiburones de La Guaira",    "VISITA", "19:00", "Meridiano TV, BeisbolPlay"),
    ("2026-11-05", "Bravos de Margarita",       "LOCAL",  "19:00", "Meridiano TV, BeisbolPlay"),
    ("2026-11-06", "Bravos de Margarita",       "LOCAL",  "19:00", "1Baseball, Meridiano TV, BeisbolPlay"),
    ("2026-11-07", "Tigres de Aragua",          "LOCAL",  "16:00", "ByM Sport, BeisbolPlay"),
    ("2026-11-08", "Tigres de Aragua",          "VISITA", "13:00", "Venevisión, BeisbolPlay"),
    ("2026-11-09", "Cardenales de Lara",        "VISITA", "19:00", "1Baseball, LVBP YouTube, BeisbolPlay"),
    ("2026-11-12", "Cardenales de Lara",        "LOCAL",  "19:00", "1Baseball, BeisbolPlay"),
    ("2026-11-13", "Cardenales de Lara",        "LOCAL",  "19:00", "ByM Sport, BeisbolPlay"),
    ("2026-11-14", "Águilas del Zulia",         "LOCAL",  "20:00", "IVC, BeisbolPlay"),
    ("2026-11-15", "Águilas del Zulia",         "LOCAL",  "16:00", "Televen, BeisbolPlay"),
    ("2026-11-16", "Cardenales de Lara",        "LOCAL",  "19:00", "1Baseball, LVBP YouTube, BeisbolPlay"),
    ("2026-11-17", "Navegantes del Magallanes", "LOCAL",  "19:00", "Venevisión, ByM Sport, BeisbolPlay"),
    ("2026-11-20", "Cardenales de Lara",        "VISITA", "19:00", "1Baseball, Meridiano TV, BeisbolPlay"),
    ("2026-11-21", "Navegantes del Magallanes", "VISITA", "20:00", "IVC, Televen, BeisbolPlay"),
    ("2026-11-24", "Navegantes del Magallanes", "VISITA", "19:00", "1Baseball, ByM Sport, Meridiano TV, BeisbolPlay"),
    ("2026-11-26", "Tigres de Aragua",          "LOCAL",  "19:00", "ByM Sport, BeisbolPlay"),
    ("2026-11-27", "Tigres de Aragua",          "LOCAL",  "19:00", "IVC, BeisbolPlay"),
    ("2026-11-28", "Cardenales de Lara",        "LOCAL",  "18:00", "Televen, BeisbolPlay"),
    ("2026-11-29", "Tiburones de La Guaira",    "LOCAL",  "13:00", "Venevisión, BeisbolPlay"),

    # ---------------- DICIEMBRE 2026 ----------------
    ("2026-12-02", "Navegantes del Magallanes", "LOCAL",  "19:00", "Televen, IVC, BeisbolPlay"),
    ("2026-12-03", "Águilas del Zulia",         "LOCAL",  "19:00", "1Baseball, BeisbolPlay"),
    ("2026-12-04", "Águilas del Zulia",         "LOCAL",  "19:00", "Venevisión, BeisbolPlay"),
    ("2026-12-05", "Caribes de Anzoátegui",     "LOCAL",  "20:00", "IVC, BeisbolPlay"),
    ("2026-12-06", "Caribes de Anzoátegui",     "LOCAL",  "17:00", "Televen, BeisbolPlay"),
    ("2026-12-08", "Caribes de Anzoátegui",     "VISITA", "19:00", "IVC, BeisbolPlay"),
    ("2026-12-09", "Caribes de Anzoátegui",     "VISITA", "19:00", "IVC, BeisbolPlay"),
    ("2026-12-10", "Bravos de Margarita",       "VISITA", "19:00", "1Baseball, BeisbolPlay"),
    ("2026-12-11", "Bravos de Margarita",       "VISITA", "19:00", "IVC, BeisbolPlay"),
    ("2026-12-12", "Tiburones de La Guaira",    "LOCAL",  "18:00", "Televen, BeisbolPlay"),
    ("2026-12-13", "Tiburones de La Guaira",    "VISITA", "13:00", "Venevisión, BeisbolPlay"),
    ("2026-12-15", "Navegantes del Magallanes", "LOCAL",  "19:00", "IVC, Televen, BeisbolPlay"),
    ("2026-12-17", "Navegantes del Magallanes", "VISITA", "19:00", "Venevisión, 1Baseball, ByM Sport, BeisbolPlay"),
    ("2026-12-18", "Tigres de Aragua",          "VISITA", "19:00", "Venevisión, BeisbolPlay"),
    ("2026-12-19", "Cardenales de Lara",        "VISITA", "20:00", "IVC, BeisbolPlay"),
    ("2026-12-20", "Cardenales de Lara",        "VISITA", "13:00", "Venevisión, BeisbolPlay"),
    ("2026-12-21", "Tigres de Aragua",          "VISITA", "19:00", "Meridiano TV, BeisbolPlay"),
    ("2026-12-22", "Tiburones de La Guaira",    "VISITA", "19:00", "ByM Sport, BeisbolPlay"),
    ("2026-12-26", "Águilas del Zulia",         "VISITA", "20:00", "IVC, BeisbolPlay"),
    ("2026-12-27", "Águilas del Zulia",         "VISITA", "17:30", "ByM Sport, BeisbolPlay"),
]

# =========================================================
# 2. ESTADIOS con ubicación/sector oficial (confirmado vía búsqueda web)
# =========================================================
# Formato: "Nombre del estadio, sector/ubicación, ciudad, estado"
# Esta es la referencia de ubicación que usan mapas (Google Maps/Waze),
# no una dirección postal con calle y número (no existe para estos recintos).

ESTADIO_LOCAL = (
    "Estadio Monumental Simón Bolívar, Sector La Rinconada, "
    "Parroquia Coche, Municipio Libertador, Caracas, Distrito Capital"
)

ESTADIOS_VISITANTES = {
    "Tiburones de La Guaira": (
        "Estadio Universitario, Ciudad Universitaria de Caracas (UCV), "
        "entre Autopista Valle-Coche y Autopista Francisco Fajardo, Caracas"
    ),
    "Tigres de Aragua": (
        "Estadio José Pérez Colmenares, Calle Campo Elías, Maracay, Aragua"
    ),
    "Águilas del Zulia": (
        "Estadio Luis Aparicio El Grande, Maracaibo, Zulia"
    ),
    "Cardenales de Lara": (
        "Estadio Antonio Herrera Gutiérrez, Sector Juan de Villegas, "
        "Barquisimeto, Lara"
    ),
    "Bravos de Margarita": (
        "Estadio Nueva Esparta, Porlamar, Isla de Margarita, Nueva Esparta"
    ),
    "Caribes de Anzoátegui": (
        "Estadio Alfonso Chico Carrasquel, Puerto La Cruz, Anzoátegui"
    ),
    "Navegantes del Magallanes": (
        "Estadio José Bernardo Pérez, Valencia, Carabobo"
    ),
}

# =========================================================
# 3. MOTOR DE GENERACIÓN .ICS
# =========================================================
def escape_ics(texto: str) -> str:
    """Escapa caracteres especiales según spec RFC 5545."""
    return (texto.replace("\\", "\\\\")
                 .replace(";", "\\;")
                 .replace(",", "\\,")
                 .replace("\n", "\\n"))


def construir_evento(fecha_str, rival, condicion, hora_str, transmision, duracion_horas=3.5):
    """
    Construye un bloque VEVENT.
    Si hora_str es None -> evento de día completo con [HORA PENDIENTE] en el título.
    Si transmision es None -> se muestra "Transmisión: por confirmar" en la descripción.
    """
    dt_inicio = datetime.strptime(fecha_str, "%Y-%m-%d")

    if condicion == "LOCAL":
        lugar = ESTADIO_LOCAL
        titulo = f"Leones del Caracas vs. {rival}"
    else:
        lugar = ESTADIOS_VISITANTES.get(rival, "Estadio por confirmar")
        titulo = f"Leones del Caracas @ {rival}"

    # UID DETERMINISTICO: se genera a partir de fecha + rival + condicion,
    # NO al azar. Esto es obligatorio para que Google Calendar reconozca
    # el mismo juego en importaciones futuras y lo ACTUALICE en vez de
    # duplicarlo cuando le agregues horas o transmision mas adelante.
    clave_evento = f"{fecha_str}-{rival}-{condicion}"
    hash_evento = hashlib.md5(clave_evento.encode("utf-8")).hexdigest()[:12]
    uid = f"{hash_evento}@calendario-republica-caraquista"
    dtstamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    if hora_str is None:
        dtstart = dt_inicio.strftime("%Y%m%d")
        dtend = (dt_inicio + timedelta(days=1)).strftime("%Y%m%d")
        titulo = f"[HORA PENDIENTE] {titulo}"
        bloque_fecha = (
            f"DTSTART;VALUE=DATE:{dtstart}\n"
            f"DTEND;VALUE=DATE:{dtend}"
        )
    else:
        hora, minuto = map(int, hora_str.split(":"))
        inicio = dt_inicio.replace(hour=hora, minute=minuto)
        fin = inicio + timedelta(hours=duracion_horas)
        bloque_fecha = (
            f"DTSTART:{inicio.strftime('%Y%m%dT%H%M%S')}\n"
            f"DTEND:{fin.strftime('%Y%m%dT%H%M%S')}"
        )

    texto_transmision = transmision if transmision else "Por confirmar"
    descripcion = (
        f"Temporada LVBP 2026/2027 - {condicion}\n"
        f"📺 Transmisión: {texto_transmision}\n"
        f"🏟️ Sede: {lugar}"
    )

    evento = (
        "BEGIN:VEVENT\n"
        f"UID:{uid}\n"
        f"DTSTAMP:{dtstamp}\n"
        f"{bloque_fecha}\n"
        f"SUMMARY:{escape_ics(titulo)}\n"
        f"LOCATION:{escape_ics(lugar)}\n"
        f"DESCRIPTION:{escape_ics(descripcion)}\n"
        "END:VEVENT"
    )
    return evento


def generar_ics(juegos, nombre_archivo="calendario_republica_caraquista.ics"):
    import os
    encabezado = (
        "BEGIN:VCALENDAR\n"
        "VERSION:2.0\n"
        "PRODID:-//Tigrin//Calendario Republica Caraquista//ES\n"
        "CALSCALE:GREGORIAN\n"
        "METHOD:PUBLISH\n"
        "X-WR-CALNAME:Calendario República Caraquista\n"
        "X-WR-CALDESC:Temporada LVBP 2026/2027 - Leones del Caracas"
    )
    pie = "END:VCALENDAR"

    eventos = [construir_evento(fecha, rival, condicion, hora, transmision)
               for fecha, rival, condicion, hora, transmision in juegos]

    contenido = "\n".join([encabezado] + eventos + [pie])

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"Archivo generado: {nombre_archivo}")

    # También actualizar automáticamente en la carpeta calendario/
    carpeta_sub = "calendario"
    if os.path.exists(carpeta_sub):
        ruta_sub = os.path.join(carpeta_sub, nombre_archivo)
        with open(ruta_sub, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"Archivo actualizado en: {ruta_sub}")

    print(f"Total de juegos exportados: {len(eventos)}")


# =========================================================
# 4. FUNCIONES PARA CARGAR HORAS Y TRANSMISIÓN DESPUÉS (sin rehacer todo)
# =========================================================
def actualizar_horas(juegos, horario_dict):
    """
    horario_dict: {"2026-10-13": "19:00", "2026-10-15": "17:00", ...}
    Devuelve una nueva lista JUEGOS con las horas inyectadas.
    Las fechas que no estén en el diccionario conservan su hora actual (o None).
    """
    actualizados = []
    for fecha, rival, condicion, hora_actual, transmision in juegos:
        nueva_hora = horario_dict.get(fecha, hora_actual)
        actualizados.append((fecha, rival, condicion, nueva_hora, transmision))
    return actualizados


def actualizar_transmisiones(juegos, transmision_dict):
    """
    transmision_dict: {"2026-10-13": "Meridiano TV", "2026-10-15": "DirecTV Sports", ...}
    Devuelve una nueva lista JUEGOS con las transmisiones inyectadas.
    Las fechas que no estén en el diccionario conservan su transmisión actual (o None).
    """
    actualizados = []
    for fecha, rival, condicion, hora, transmision_actual in juegos:
        nueva_transmision = transmision_dict.get(fecha, transmision_actual)
        actualizados.append((fecha, rival, condicion, hora, nueva_transmision))
    return actualizados


# =========================================================
# EJECUCIÓN
# =========================================================
if __name__ == "__main__":
    # La LVBP anunció el patrón general de horarios (no las horas exactas por juego):
    #   Lunes a viernes: 7:00 p.m.
    #   Fines de semana: 1:00, 3:00, 5:00, 7:00 u 8:00 p.m. según jornada y estadio
    # Agrega aquí las horas confirmadas del fixture oficial cuando las tengas:
    horarios_conocidos = {
        # "2026-10-13": "19:00",
    }

    # Agrega aquí las transmisiones (canal/streaming) cuando las tengas:
    transmisiones_conocidas = {
        # "2026-10-13": "Meridiano TV",
    }

    juegos_actualizados = actualizar_horas(JUEGOS, horarios_conocidos)
    juegos_actualizados = actualizar_transmisiones(juegos_actualizados, transmisiones_conocidas)
    generar_ics(juegos_actualizados)

    # ---------------------------------------------------------------
    # OPCIONAL: hacer commit y push automático a un repo de GitHub
    # para que la URL raw se actualice sola sin pasos manuales.
    # Requiere que este script corra dentro de un repo git ya
    # configurado (con remote y credenciales/SSH listos).
    # Actívalo cambiando AUTO_PUSH a True.
    # ---------------------------------------------------------------
    AUTO_PUSH = False

    if AUTO_PUSH:
        import subprocess

        archivo = "calendario_republica_caraquista.ics"
        try:
            subprocess.run(["git", "add", archivo], check=True)
            resultado = subprocess.run(
                ["git", "commit", "-m", "Actualizacion automatica del calendario"],
                capture_output=True, text=True
            )
            if resultado.returncode != 0:
                print("Sin cambios que commitear (el archivo no cambió).")
            else:
                subprocess.run(["git", "push"], check=True)
                print("Push realizado. La URL raw se actualizará en unos minutos.")
        except subprocess.CalledProcessError as e:
            print(f"Error al hacer commit/push: {e}")
            print("Revisa que el repo tenga remote configurado y credenciales válidas.")
