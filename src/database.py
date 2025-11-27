import sqlite3
import os

# Ruta absoluta a la base de datos
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "cafeteria.db")

# Conexión
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Crear tabla de productos
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL
)
''')

# Crear tabla de ventas
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER,
    cantidad INTEGER,
    total REAL,
    FOREIGN KEY (producto_id) REFERENCES productos(id)
)
''')

conn.commit()
