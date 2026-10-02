import csv
import json
from pathlib import Path

# Configurar las rutas
BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "datos" / "estudiantes.csv"
RUTA_JSON = BASE_DIR / "salida" / "estudiantes_resumen.json"

# Paso 4: Función de transformación
def transformar_estudiante(registro: dict) -> dict:
    estado_texto = "Activo" if registro["activo"].lower() == "true" else "Inactivo"
    return {
        "id": registro["codigo"],
        "nombre_completo": f"{registro['nombre']} {registro['apellido']}",
        "semestre": int(registro["semestre"]),
        "promedio": float(registro["promedio"]),
        "estado": estado_texto
    }

# Paso 6: Función para guardar en JSON
def serializar_estudiantes(ruta: Path, estudiantes: list[dict]) -> None:
    """Serializa una lista de diccionarios Python a un archivo JSON UTF-8."""
    ruta.parent.mkdir(exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=2, ensure_ascii=False)

# Paso 7: Función para leer desde JSON
def deserializar_estudiantes(ruta: Path) -> list[dict]:
    """Deserializa un archivo JSON a una lista de diccionarios Python."""
    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)

# --- FLUJO PRINCIPAL ---

# 1. Leer y transformar los datos
estudiantes_transformados = []
with open(RUTA_CSV, mode="r", encoding="utf-8") as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        estudiantes_transformados.append(transformar_estudiante(fila))

# 2. Guardar el archivo JSON
serializar_estudiantes(RUTA_JSON, estudiantes_transformados)
print(f"Archivo JSON generado: {RUTA_JSON}")

# 3. Leer el JSON para comprobar
estudiantes_recuperados = deserializar_estudiantes(RUTA_JSON)
print("\nDatos recuperados desde el JSON:")
print(estudiantes_recuperados[0])
print(f"Total recuperado: {len(estudiantes_recuperados)}")