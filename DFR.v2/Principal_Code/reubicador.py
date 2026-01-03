import shutil
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
CARPETA_REPORTES = BASE_DIR / "Reportes"

def importar_archivo_por_rango(nombre_rango):
    """
    Busca en Descargas archivos que contengan la palabra clave 
    Y que hayan sido modificados el día de HOY.
    """
    carpeta_descargas = Path.home() / "Downloads"
    CARPETA_REPORTES.mkdir(parents=True, exist_ok=True)

    palabra = nombre_rango.lower()
    
    # 1. Obtenemos la fecha de hoy en formato YYYY-MM-DD para comparar
    hoy = datetime.now().date()

    # 2. Filtrar archivos: que contengan la palabra Y sean de hoy
    archivos_hoy = []
    for f in carpeta_descargas.iterdir():
        if f.is_file() and palabra in f.name.lower():
            # Obtener fecha de modificación del archivo
            fecha_modificacion = datetime.fromtimestamp(f.stat().st_mtime).date()
            
            if fecha_modificacion == hoy:
                archivos_hoy.append(f)

    if not archivos_hoy:
        # Aquí podrías lanzar uno de tus "errores programados"
        print(f"No se encontraron archivos de hoy con la palabra: {palabra}")
        return []

    rutas_finales = []

    for archivo in archivos_hoy:
        destino = CARPETA_REPORTES / archivo.name
        
        # Copiar y preservar metadatos
        shutil.copy2(str(archivo), str(destino))
        
        # Eliminar el original
        archivo.unlink()
        
        rutas_finales.append(destino)
        print(f"Archivo procesado: {archivo.name}")

    return rutas_finales