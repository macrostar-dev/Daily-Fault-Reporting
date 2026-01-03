from reubicador import *
from filler import generar_reporte_ko_misma_carpeta
from conversor import procesar_archivo
from login import login_automatico
from correo import enviar_correo_con_adjuntos
from notification import enviar_mensaje
from archivo_diario import copiar_archivo_con_fecha
from eliminador import *
from dotenv import load_dotenv
from actualizador_anual import actualizacion_anual
import os
import traceback
import logging

load_dotenv()

# -------- LOG --------
logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------- NOTIFICACIÓN --------
def enviar_notificacion(error):
    print("⚠️ Proceso cancelado por error")
    print(error)
    mensaje_final = f"Error en automatización\n{error}"
    logging.error(mensaje_final)
    enviar_mensaje(
    WEBEX_TOKEN=os.getenv("WEBEX_TOKEN"), 
    WEBEX_ROOM_ID=os.getenv("WEBEX_ROOM_ID"),    
    mensaje=(mensaje_final))


# -------- PIPELINE --------
def ejecutar_pipeline():
    try:
        # 1. Preparación Inicial
        print("🚀 Iniciando Pipeline...")
        actualizacion_anual()

        # 2. Navegación y Login
        # Nota: Si login_automatico falla, saltará directo al 'except'
        login_automatico(
            url_login=os.getenv("URL_LOGIN"),
            usuario_texto=os.getenv("USUARIO_TEXTO"),
            password_texto=os.getenv("PASSWORD_TEXTO"),
            url_destino=os.getenv("URL_DESTINO"),
            url_destino2=os.getenv("URL_DESTINO2")
        )

        # 3. Procesamiento de archivos
        importar_archivo_por_rango("Grecia")
        importar_archivo_por_rango("Desamparados")
        procesar_archivo('grecia', 'Grecia')
        procesar_archivo('desamparados', 'Desamparados')

        # 4. Consolidación de Reportes
        nombre_base = "Monitoreo Diario U-Admin Grecia-Desamparados.xlsx"
        
        generar_reporte_ko_misma_carpeta(
            archivo_origen="Reportes/Grecia.xlsx",
            archivo_destino=nombre_base,
            hoja_destino="Grecia",
        )
        
        generar_reporte_ko_misma_carpeta(
            archivo_origen="Reportes/Desamparados.xlsx",
            archivo_destino=nombre_base,
            hoja_destino="Desamparados",
        )

        # 5. Generar archivo con fecha (IMPORTANTE: Capturamos el nombre)
        documento = copiar_archivo_con_fecha("Monitoreo Diario U-Admin Grecia-Desamparados")

        # 6. Envío de Correo (Usamos la variable 'documento' que acabamos de crear)
        ruta_completa = Path(__file__).resolve().parent.parent / documento
        
        enviar_correo_con_adjuntos(
            destinatario="correo",
            asunto="Reporte Diario de parquimetro",
            cuerpo="Buenas tardes,\n\nSe adjunta el documento...\n\nSaludos.",
            ruta_archivo=ruta_completa,
            cc=["correo"]
        )

        # 7. Limpieza y Notificación Final
        eliminar_archivo_por_palabra(palabra_buscar=fecha_del_documento)

        enviar_mensaje(
            WEBEX_TOKEN=os.getenv("WEBEX_TOKEN"), 
            WEBEX_ROOM_ID=os.getenv("WEBEX_ROOM_ID"),    
            mensaje=(
                "✅ El correo del reporte de Uadmin se ha enviado exitosamente.\n"
                f"⏱️ Hora de envío: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
        )
        print("✨ Proceso completado con éxito.")

    except Exception as e:
        # Si CUALQUIER paso anterior falla, se ejecuta esto:
        error_detallado = traceback.format_exc()
        enviar_notificacion(error_detallado)
        
        # Opcional: Avisar por Webex que el proceso falló
        # enviar_mensaje(..., mensaje=f"❌ Error en el proceso: {e}")

if __name__ == "__main__":
    ejecutar_pipeline()


