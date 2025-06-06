# main.py
import flet as ft
from utils import route_change  # <-- Usa o seu arquivo de roteamento


def main(page: ft.Page):
    page.title = 'AcadeGUIA'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.favicon = 'assets/favicon.png'
    page.theme_mode = ft.ThemeMode.DARK

    page.fonts = {
        'RobotoSlab': 'https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf'
    }
    page.theme = ft.Theme(font_family='RobotoSlab')

    # IMPORTANTE: A página não tem mais conteúdo fixo.
    # O conteúdo agora é 100% controlado pelo route_change.

    page.on_route_change = lambda e: route_change(page)
    page.go(page.route)


# Mantive a sua configuração do ft.app
ft.app(view=ft.AppView.FLET_APP, target=main, assets_dir='assets')
