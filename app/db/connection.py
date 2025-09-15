# app/db/connection.py
import pymysql
import config

def get_connection():
    return pymysql.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,  # resultados como dict
    )

def test_connection():
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * from Users")
            result = cursor.fetchone()
        conn.close()
        print("✅ Conexión exitosa:", result)
    except Exception as e:
        print("❌ Error de conexión:", e)
