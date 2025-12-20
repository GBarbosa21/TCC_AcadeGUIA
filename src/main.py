import flet as ft
from utils import route_change
# 1. Importe a função que popula o banco
from database.seed import inicializar_catalogo


def main(page: ft.Page):
    page.title = 'AcadeGUIA'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.favicon = 'assets/favicon.png'
    page.theme_mode = ft.ThemeMode.DARK

    page.fonts = {
        'RobotoSlab': 'https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf'
    }
    page.theme = ft.Theme(font_family='RobotoSlab')

    page.on_route_change = lambda e: route_change(page)
    page.go(page.route)


# 2. Execute a população do banco ANTES de iniciar o app
if __name__ == "__main__":
    # Garante que o catálogo de exercícios existe
    print("Verificando banco de dados...")
    inicializar_catalogo()

    # Inicia o app
    ft.app(target=main, assets_dir='assets')