import flet as ft

# Tratamento de importações
try:
    from funcoes import layout_com_header_fixado, nav_bar, botao_menu_principal
    from Styles import EstiloTxt
except ImportError:
    from src.funcoes import layout_com_header_fixado, nav_bar, botao_menu_principal
    from src.Styles import EstiloTxt

def inicio(page: ft.Page):
    """Constrói a View da página inicial."""

    conteudo = [
        ft.Image(
            # CORRIGIDO: Removemos 'assets/' do caminho.
            # O Flet já sabe que está na pasta assets.
            src='AcadeGUIA.png',
            fit=ft.ImageFit.CONTAIN,
            height=240
        ),
        # Container para garantir o alinhamento e espaçamento corretos
        ft.Container(
            width=320,
            alignment=ft.alignment.center,
            content=ft.Column(
                spacing=15,
                controls=[
                    botao_menu_principal(
                        texto='Minhas Séries',
                        icone=ft.Icons.ARCHIVE_OUTLINED,
                        on_click=lambda e: e.page.go('/minhas_series'),
                    ),
                    botao_menu_principal(
                        texto='Exercícios',
                        icone=ft.Icons.FITNESS_CENTER,
                        on_click=lambda e: e.page.go('/exercicios'),
                    ),
                    botao_menu_principal(
                        texto='Exercícios Salvos',
                        icone=ft.Icons.BOOKMARK_BORDER,
                        on_click=lambda e: e.page.go('/exercicios_salvos')
                    ),
                ],
            ),
        ),
    ]

    return layout_com_header_fixado(
        page,
        'ACADEGUIA',
        conteudo,
        bottom=nav_bar(page, selected_index=1)
    )