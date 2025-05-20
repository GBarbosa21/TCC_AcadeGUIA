import flet as ft

from src.funcoes import *


def minhas_series():
    return layout_com_header_fixado(
        "Minhas Séries",
    [
        criar_card_serie("Peito", 4),
        criar_card_serie("Costas", 5)
    ],
    nav_bar
)