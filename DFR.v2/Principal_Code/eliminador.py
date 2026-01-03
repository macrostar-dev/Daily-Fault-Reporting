from pathlib import Path
from datetime import datetime

fecha_hoy = datetime.now().strftime("%d/%m/%Y")   
fecha_del_documento= fecha_hoy.replace("/", "-")   

BASE_DIR = Path(__file__).resolve().parent.parent
CARPETA_TRABAJO = BASE_DIR   

def eliminar_archivo_por_palabra(palabra_buscar: str):

    if not CARPETA_TRABAJO.exists():
        raise FileNotFoundError(f"❌ La carpeta base no existe: {CARPETA_TRABAJO}")

    # 1. Buscar archivo que contenga la palabra clave
    archivo_a_borrar = next(
        (
            f for f in CARPETA_TRABAJO.iterdir()
            if f.is_file() and palabra_buscar in f.name.lower()
        ),
        None
    )

    if not archivo_a_borrar:
        print(f"❌ No se encontró archivo que contenga: '{palabra_buscar}'")
        return

    print(f"🗑 Archivo encontrado para eliminar: {archivo_a_borrar.name}")

    # 2. Eliminar archivo
    try:
        archivo_a_borrar.unlink()
        print(f"✔ Archivo eliminado: {archivo_a_borrar.name}")
    except Exception as e:
        print(f"❌ Error al eliminar el archivo: {e}")

