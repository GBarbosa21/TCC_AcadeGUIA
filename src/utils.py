from PIL import Image
import flet as ft
from funcoes import container, nav_bar
from Styles import EstiloTxt

def route_change(page: ft.Page):
    if page.route == "/":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[container, nav_bar],
            )
        )
    elif page.route == "/minhas_series":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/minhas_series",
                controls=[
                    nav_bar,
                    ft.Text("Conteúdo da página de Treino A", style=EstiloTxt),
                    ft.ElevatedButton("Voltar", on_click=lambda e: page.go("/"))
                ],
            )
        )

    page.update()