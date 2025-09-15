import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Directorio de logs
LOG_DIR = os.getenv("LOG_DIR", "./logs")  # fallback a ./logs si no está definido
os.makedirs(LOG_DIR, exist_ok=True)       # asegura que exista la carpeta
