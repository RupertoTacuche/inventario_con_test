import flet as ft

def crear_vista(page: ft.Page, controller):
    page.title = "Control de Inventario"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20
    
    # Activamos el modo oscuro y configuramos el fondo azul marino oscuro (#0b192c o similar)
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0B192C" # Azul marino oscuro profundo

    # Campos de entrada con estilo adaptado
    txt_nombre = ft.TextField(
        label="Nombre del producto", 
        width=300,
        border_color=ft.Colors.WHITE,
        focused_border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        color=ft.Colors.WHITE
    )
    txt_stock = ft.TextField(
        label="Stock", 
        value="0", 
        width=140, 
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color=ft.Colors.WHITE,
        focused_border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        color=ft.Colors.WHITE
    )
    txt_precio = ft.TextField(
        label="Precio ($)", 
        value="0.0", 
        width=140, 
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color=ft.Colors.WHITE,
        focused_border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        color=ft.Colors.WHITE
    )
    
    lbl_mensaje = ft.Text(value="", color=ft.Colors.GREEN_ACCENT)
    
    # Lista visual de productos
    lista_view = ft.ListView(expand=1, spacing=8, padding=10, auto_scroll=True)

    def actualizar_lista():
        lista_view.controls.clear()
        productos = controller.obtener_lista_productos()
        for prod in productos:
            _, nom, stock, prec = prod
            lista_view.controls.append(
                ft.Card(
                    color="#1E3E62", # Un tono azul marino un poco más claro para las tarjetas
                    elevation=4,
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(f"📦 {nom}", weight=ft.FontWeight.BOLD, size=16, color=ft.Colors.WHITE),
                            ft.Row([
                                ft.Text(f"Stock: {stock}", color=ft.Colors.WHITE70),
                                ft.Text(f"Precio: ${prec:.2f}", color=ft.Colors.WHITE70)
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        ]),
                        padding=12
                    )
                )
            )
        page.update()

    def btn_guardar_click(e):
        exito, mensaje = controller.agregar_producto(
            txt_nombre.value, 
            txt_stock.value, 
            txt_precio.value
        )
        
        if exito:
            lbl_mensaje.color = ft.Colors.GREEN_ACCENT
            lbl_mensaje.value = mensaje
            txt_nombre.value = ""
            txt_stock.value = "0"
            txt_precio.value = "0.0"
            actualizar_lista()
        else:
            lbl_mensaje.color = ft.Colors.RED_ACCENT
            lbl_mensaje.value = mensaje
        page.update()

    btn_guardar = ft.ElevatedButton(
        "Guardar Producto", 
        on_click=btn_guardar_click, 
        icon=ft.Icons.SAVE,
        color=ft.Colors.WHITE,
        bgcolor="#1E3E62"
    )

    # Cargar datos iniciales
    actualizar_lista()

    # Retornar la estructura principal de la pantalla
    return ft.Column([
        ft.Text("Mi Inventario Móvil", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
        txt_nombre,
        ft.Row([txt_stock, txt_precio], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        btn_guardar,
        lbl_mensaje,
        ft.Divider(color=ft.Colors.WHITE24),
        ft.Text("Productos Registrados:", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
        lista_view
    ], expand=True)