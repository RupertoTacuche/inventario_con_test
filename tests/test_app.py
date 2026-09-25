import os
import pytest
from controllers import InventarioController
from models import init_db, DB_NAME

@pytest.fixture(autouse=True)
def limpiar_db():
    # Asegurar base de datos limpia para pruebas
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    init_db()
    yield

def test_agregar_producto_valido():
    controller = InventarioController()
    exito, mensaje = controller.agregar_producto("Desarmador", "10", "45.50")
    assert exito is True
    
    productos = controller.obtener_lista_productos()
    assert len(productos) == 1
    # Corregido: accedemos a la primera fila [0] y a la columna del nombre [1]
    assert productos[0][1] == "Desarmador"
    assert productos[0][2] == 10
    assert productos[0][3] == 45.50

def test_agregar_producto_invalido_nombre_vacio():
    controller = InventarioController()
    exito, mensaje = controller.agregar_producto("", "5", "10.0")
    assert exito is False
    assert "vacío" in mensaje

def test_agregar_producto_invalido_stock_letras():
    controller = InventarioController()
    exito, mensaje = controller.agregar_producto("Martillo", "abc", "10.0")
    assert exito is False
    assert "entero" in mensaje