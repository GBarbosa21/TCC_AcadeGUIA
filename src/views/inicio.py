# inicio.py
import flet as ft
from ..funcoes import layout_com_header_fixado, nav_bar, botao_menu_principal
from ..Styles import EstiloTxt


def inicio(page: ft.Page):
    """Constrói a View da página inicial."""

    conteudo = [
        ft.Image(
            src='assets/AcadeGUIA.png', fit=ft.ImageFit.CONTAIN, height=240
        ),
        # Container para garantir o alinhamento e espaçamento corretos
        ft.Container(
            width=320,
            alignment=ft.alignment.center,
            content=ft.Column(
                spacing=15,
                controls=[
                    # MUDANÇA: Usando a nova função para criar botões com o estilo do protótipo
                    botao_menu_principal(
                        texto='Minhas Séries',
                        icone=ft.icons.ARCHIVE_OUTLINED,
                        on_click=lambda e: e.page.go('/minhas_series'),
                    ),
                    botao_menu_principal(
                        texto='Exercícios',
                        icone=ft.icons.FITNESS_CENTER,
                        on_click=lambda e: e.page.go('/exercicios'),
                    ),
                    botao_menu_principal(
                        texto='Exercícios Salvos',
                        icone=ft.icons.BOOKMARK_BORDER,
                        on_click=lambda e: print(
                            'Navegar para Exercícios Salvos'
                        ),
                    ),
                ],
            ),
        ),
    ]

    return layout_com_header_fixado(
        page, 'ACADEGUIA', conteudo, bottom=nav_bar(page, selected_index=1)
    )
