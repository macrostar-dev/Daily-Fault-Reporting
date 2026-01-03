Sistema de Automatización de Reportes (V2)
Este sistema automatiza la descarga, procesamiento, consolidación y envío de reportes operativos. La versión 2 introduce un manejo de errores robusto, logs de sistema y mayor seguridad mediante variables de entorno.

🚀 Flujo Principal (test.py / Pipeline)
El sistema ahora opera bajo un Pipeline que garantiza que si un paso falla, se notifique inmediatamente y se registre el error:

Mantenimiento: Ejecuta el actualizador_anual.py para archivar datos del año anterior si es necesario.

Extracción Web: Acceso automatizado mediante Selenium para descargar los reportes del día.

Gestión de Descargas: Identifica los archivos descargados hoy en la carpeta de sistema y los traslada al entorno local.

Transformación de Datos:

Convierte y renombra archivos a formato .xlsx.

Filtra filas específicas (registros "KO") y las inserta en el documento maestro de monitoreo.

Distribución:

Crea una copia de seguridad con la fecha actual.

Envía el reporte por correo electrónico (Outlook/Office 365).

Cierre: Elimina archivos temporales y envía una confirmación de éxito o un reporte de error detallado a Webex.

📂 Descripción de Módulos
🛠️ Núcleo y Control
test.py: Es el nuevo orquestador. Implementa un bloque try/except global que captura cualquier fallo, genera un log en errores.log y envía una notificación de alerta con el error exacto.
actualizador_anual.py: Gestiona el ciclo de vida anual de los documentos, moviendo archivos al Registro_Anual y limpiando las plantillas para el nuevo periodo.

🌐 Automatización y Scraping
login.py: Controla el navegador en modo headless. Utiliza inyección de JavaScript para interactuar con elementos complejos y disparar las descargas de forma eficiente.
reubicador.py: Escanea la carpeta de descargas del sistema buscando archivos modificados el día de hoy que coincidan con las palabras clave configuradas.
📊 Procesamiento de Datos
filler.py: Realiza el mapeo de columnas entre el reporte crudo y el formato final. Añade metadatos como fecha, hora de inserción y estados automáticos (ej. "Desconectado").
conversor.py: Asegura la integridad de las extensiones de archivo y prepara los documentos para la manipulación con openpyxl.

✉️ Comunicación y Seguridad
correo.py: Módulo de mensajería SMTP que ahora utiliza variables de entorno para proteger las credenciales.
notification.py: Cliente para la API de Webex que envía mensajes de estado (éxito/error) a salas específicas.
.env (Archivo de configuración): Almacena tokens, contraseñas y IDs de sala de forma segura (no debe subirse al control de versiones).

🔧 Configuración Requerida
Variables de Entorno
Crea un archivo .env en la raíz con:

Fragmento de código

USER_MAIL=tu_correo@ejemplo.com
USER_PASSWORD=tu_contraseña_de_aplicacion
WEBEX_TOKEN=tu_token_de_webex
WEBEX_ROOM_ID=id_de_la_sala
