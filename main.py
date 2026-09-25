import flet as ft
from controllers import InventarioController
from views import crear_vista

def main(page: ft.Page):
    controller = InventarioController()
    vista = crear_vista(page, controller)
    page.add(vista)

if __name__ == "__main__":
    ft.app(target=main)