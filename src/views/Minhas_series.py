# Minhas_series.py
import flet as ft
from funcoes import (
    layout_com_header_fixado,
    nav_bar,
    btn_nova_serie,
    criar_card_serie,
)


def minhas_series(page: ft.Page):   # <-- Agora recebe 'page'
    conteudo = [
        btn_nova_serie(on_click=lambda e: print('Abrir tela de nova série')),
        criar_card_serie(
            'Peito',
            4,
            on_click=lambda e: e.page.go('/serie'),
            on_delete=lambda: print('Excluir série Peito'),
        ),
        criar_card_serie(
            'Costas',
            5,
            on_click=lambda e: e.page.go('/serie'),
            on_delete=lambda: print('Excluir série Costas'),
        ),
    ]

    # <-- Chamada da função de layout corrigida
    return layout_com_header_fixado(
        page,
        'Minhas Séries',
        conteudo,
        # MUDANÇA: O índice de "Minhas Séries" agora é 2
        bottom=nav_bar(page, selected_index=2),
    )
