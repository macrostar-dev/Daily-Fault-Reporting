Sistema de Automatización de Reportes
Este proyecto es una solución integral en Python diseñada para automatizar el ciclo de vida de los reportes operativos: desde la extracción de datos mediante navegación web hasta el procesamiento de hojas de cálculo y la notificación de resultados.

🚀 Flujo de Trabajo (Script: hard.py)
Mantenimiento Temporal: Al iniciar, el sistema verifica si es necesario realizar un respaldo anual y resetear las plantillas de trabajo.
Extracción Web: Utiliza automatización de navegador para acceder a portales internos, navegar a secciones específicas y descargar los datos más recientes.
Preparación de Archivos: Localiza los archivos descargados, los mueve al directorio de trabajo y asegura que tengan el formato .xlsx correcto.
Procesamiento de Datos: Analiza los archivos origen, filtra filas bajo criterios específicos (ej. registros con estado "KO") y consolida la información en un documento maestro.
Distribución y Notificación: Genera una copia fechada del reporte final, la envía por correo electrónico a los destinatarios configurados y emite una alerta de éxito vía mensajería instantánea.
Limpieza: Elimina los archivos temporales creados durante la ejecución para optimizar el espacio.

📂 Descripción de los Módulos
1. Automatización de Navegador (login.py)
Gestiona el inicio de sesión automático y la interacción con elementos de la interfaz web.
Ejecuta scripts de consola (JavaScript) para forzar descargas o acciones específicas en el portal.
Utiliza un modo "sin cabeza" (headless) para ejecutarse en servidores sin interfaz gráfica.

2. Procesamiento de Excel (filler.py, conversor.py)
Transformación: Convierte archivos genéricos descargados en libros de Excel válidos.
Lógica de Inserción: Busca celdas vacías en documentos de destino para insertar nuevos datos sin sobrescribir información previa.
Filtrado: Identifica y extrae exclusivamente las filas que requieren atención técnica.

3. Gestión de Archivos (reubicador.py, archivo_diario.py, eliminador.py)
Organización: Monitorea la carpeta de descargas del usuario y mueve los reportes detectados al entorno de trabajo.
Versionado: Crea copias de seguridad diarias incluyendo la fecha en el nombre del archivo para mantener un historial.
Mantenimiento: Incluye funciones para borrar archivos específicos basados en palabras clave o patrones de nombre.

4. Comunicaciones (correo.py, notification.py)
Envío de Mail: Soporta el envío de correos con archivos adjuntos y copia (CC) a múltiples usuarios vía SMTP.
Alertas API: Se integra con servicios de mensajería (Webex) mediante peticiones HTTP para confirmar la finalización del proceso en tiempo real.

6. Control Anual (actualizador_anual.py)
Ejecuta una rutina especial cada 1 de enero para archivar el registro del año saliente y limpiar las filas de los documentos de trabajo activos, preparándolos para el nuevo ciclo.

🛠️ Requisitos del Sistema
Python 3.x
Librerías: selenium, openpyxl, requests, shutil.
Navegador: Google Chrome y su respectivo WebDriver.
