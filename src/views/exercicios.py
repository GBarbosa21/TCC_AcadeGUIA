# serie.py
import flet as ft
from ..funcoes import layout_com_header_fixado, nav_bar, btn_info_exercicio


def exercicio_info(page: ft.Page):
    """Constrói a View que lista os exercicios"""

    # Conteúdo alinhado com o protótipo da página "Exercicio"
    conteudo = [
        # Cabeçalho com o nome da série e o ícone de check
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Título da série, como "Exercicios"
                ft.Text(
                    'Exercicios',
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color='#A6A6F6',
                ),
            ],
        ),
        # Linha divisória
        ft.Container(height=1, width=200, bgcolor='#A6A6F6'),
        # Cards de exercícios da série
        btn_info_exercicio(
            'Supino Reto',
            on_click=lambda e: e.page.go('/detalhes_exercicio'),
            on_Save=lambda e: e.page.go('/exercicios_salvos'),
            on_Play=lambda e: e.page.go('/detalhes_exercicio')
        ),
        btn_info_exercicio(
            'Supino Inclinado',
            on_click=lambda e: print('supino inclinado'),
            on_Save=lambda e: e.page.go('/exercicios_salvos'),
            on_Play=lambda e: print('Play')
        ),
    ]

    return layout_com_header_fixado(
        page,
        'Exercícios',
        conteudo,
        # O indíce de navbar é 0 selecionando essa pagina de série
        bottom=nav_bar(page, selected_index=0),
    )
