import flet as ft
from funcoes import *

def main(page: ft.Page):
    page.title="AcadeGUIA"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.favicon="assets/favicon.png"
    page.window.width = 500
    page.window.height = 800

    page.fonts = {
        "Codystar": "fonts/Codystar-Regular.ttf"
    }

    page.add(app_bar, container, nav_bar)
    page.theme = ft.Theme(font_family="Codystar")
    page.bg_color = ft.Colors.GREY


ft.app(view=ft.AppView.FLET_APP, target=main, assets_dir="assets")
