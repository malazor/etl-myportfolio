import pandas as pd
import os

def log_to_csv(log_path: str) -> str:
    """
    Convierte un log en formato JSON (1 línea = 1 objeto)
    en un CSV guardado en la carpeta ../csv/
    """
    if not os.path.exists(log_path):
        raise FileNotFoundError(f"No existe el archivo: {log_path}")

    # Crear carpeta csv si no existe
    base_dir = os.path.dirname(os.path.dirname(log_path))  # sube un nivel desde logs/
    csv_dir = os.path.join(base_dir, "csv")
    os.makedirs(csv_dir, exist_ok=True)

    # Nombre base del archivo
    filename = os.path.basename(log_path).replace(".log", ".csv")
    csv_path = os.path.join(csv_dir, filename)

    # Leer log JSON y exportar
    df = pd.read_json(log_path, lines=True)
    df.to_csv(csv_path, index=False)

    return csv_path

if __name__ == "__main__":
    ruta = input("Ruta del log JSON a convertir: ").strip()
    try:
        salida = log_to_csv(ruta)
        print(f"CSV generado en: {salida}")
    except Exception as e:
        print(f"Error: {e}")
