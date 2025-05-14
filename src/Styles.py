import flet as ft
from flet.core.padding import Padding
from flet.core.text_style import TextStyle

btn_exerc_style = ft.ButtonStyle(
    color={
        ft.ControlState.DEFAULT: ft.Colors.LIGHT_BLUE_800,
        ft.ControlState.HOVERED: ft.Colors.LIGHT_BLUE_700,
    },
    padding={
        ft.ControlState.DEFAULT: ft.Padding(
            top=20, right=20, bottom=20, left=20
        ),
        ft.ControlState.HOVERED: ft.Padding(
            top=50, right=20, bottom=50, left=20
        ),
    },
    animation_duration=500,
)

EstiloTxt = ft.TextStyle(
    font_family='RobotoSlab', size=45, weight=ft.FontWeight.BOLD, italic=True
)
