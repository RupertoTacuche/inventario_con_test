from models import init_db, db_agregar_producto, db_obtener_productos, DB_NAME
import sqlite3
class InventarioController:
    def __init__(self):
        init_db()

    def agregar_producto(self, nombre, stock_str, precio_str):
        """Valida y procesa la inserción de un producto."""
        if not nombre:
            return False, "El nombre no puede estar vacío."
        
        try:
            stock = int(stock_str)
            precio = float(precio_str)
            if stock < 0 or precio < 0:
                return False, "Stock y precio deben ser mayores o iguales a 0."
        except ValueError:
            return False, "Stock debe ser entero y precio numérico."

        db_agregar_producto(nombre, stock, precio)
        return True, "Producto agregado con éxito."
    
    def eliminar_producto(self, id_producto):
    # Conexión a SQLite y ejecución del DELETE
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        conexion.close()

    def obtener_lista_productos(self):
        return db_obtener_productos()