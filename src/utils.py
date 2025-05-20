import flet as ft
from funcoes import container, nav_bar
from PIL import Image
from Styles import EstiloTxt

from views.Minhas_series import minhas_series


def route_change(page: ft.Page):
    if page.route == '/':
        page.views.clear()
        page.views.append(
            ft.View(
                route='/',
                controls=[container, nav_bar],
            )
        )
    elif page.route == '/minhas_series':
        page.views.clear()
        page.views.append(minhas_series())


    page.update()
