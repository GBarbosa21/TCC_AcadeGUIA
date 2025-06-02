from src.funcoes import *


def serie():
    return layout_com_header_fixado(
        'Série',
        [
            header_editavel('Peito', on_click=lambda e: e.page.go('/serie')),
            card_exercicio(
                'Supino Inclinado', 4, 12, on_click=lambda e: print('supino')
            ),
            card_exercicio(
                'Supino Reto', 4, 12, on_click=lambda e: print('supino')
            ),
        ],
        nav_bar,
    )
