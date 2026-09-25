import sqlite3

DB_NAME = "inventario_flet.db"

def init_db():
    """Inicializa la base de datos y la tabla de productos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            stock INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def db_agregar_producto(nombre, stock, precio):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)", (nombre, stock, precio))
    conn.commit()
    conn.close()

def db_obtener_productos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, stock, precio FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos