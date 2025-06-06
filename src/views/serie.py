# serie.py
import flet as ft
from ..funcoes import layout_com_header_fixado, nav_bar, card_exercicio


def serie(page: ft.Page):
    """Constrói a View que detalha uma série específica, baseada no protótipo."""

    # Conteúdo alinhado com o protótipo da página "Série"
    conteudo = [
        # Cabeçalho com o nome da série e o ícone de check
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Título da série, como "Peito"
                ft.Text(
                    'Peito',
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color='#A6A6F6',
                ),
                # Ícone de check no canto, conforme protótipo
                ft.IconButton(
                    icon=ft.icons.CHECK_CIRCLE_OUTLINE,
                    icon_color=ft.colors.GREEN,
                    icon_size=30,
                    tooltip='Salvar Alterações',
                ),
            ],
        ),
        # Linha divisória
        ft.Container(height=1, width=200, bgcolor='#A6A6F6'),
        # Cards de exercícios da série
        card_exercicio(
            'Supino Inclinado',
            4,
            12,
            on_click=lambda e: print('supino inclinado'),
        ),
        card_exercicio(
            'Supino Reto', 4, 12, on_click=lambda e: print('supino reto')
        ),
        card_exercicio(
            'Voador Peitoral', 4, 12, on_click=lambda e: print('voador')
        ),
    ]

    return layout_com_header_fixado(
        page,
        'Série',
        conteudo,
        # MUDANÇA: O índice continua sendo o de "Minhas Séries", que agora é 2
        bottom=nav_bar(page, selected_index=2),
    )
