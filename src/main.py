import flet as ft
from funcoes import *
from utils import route_change


def main(page: ft.Page):
    page.title = "AcadeGUIA"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.favicon = "assets/favicon.png"

    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }

    page.theme = ft.Theme(font_family="RobotoSlab")
    page.bg_color = ft.Colors.GREY_100  # cor cinza mais clara pra ficar mais bonito

    page.add(container, nav_bar)

    page.on_route_change = lambda e: route_change(page)
    page.go(page.route)

ft.app(view=ft.AppView.FLET_APP, target=main, assets_dir="assets")