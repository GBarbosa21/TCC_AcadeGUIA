# serie.py
import flet as ft
from ..funcoes import layout_com_header_fixado, nav_bar, btn_info_exercicio_salvos


def exercicios_salvos_info(page: ft.Page):
    """Constrói a View que lista os exercicios Salvos"""

    conteudo = [
        # Cabeçalho com o nome da série e o ícone de check
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Título da série, como "Exercicios - Salvos"
                ft.Text(
                    'Exercicios - Salvos',
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color='#A6A6F6',
                ),
            ],
        ),
        # Linha divisória
        ft.Container(height=1, width=200, bgcolor='#A6A6F6'),
        # Cards de exercícios da série
        btn_info_exercicio_salvos(
            'Supino Reto',
            on_click=lambda e: print('supino reto'),
            on_Delete=lambda e: print('Delete'),
            on_Play=lambda e: print('Play')
        ),
    ]

    return layout_com_header_fixado(
        page,
        'Série',
        conteudo,
        # O indíce de navbar é 0 selecionando essa pagina de série
        bottom=nav_bar(page, selected_index=0),
    )
