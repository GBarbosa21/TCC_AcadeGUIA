import flet as ft

btn_exerc_style= ft.ButtonStyle(
        color={
            ft.ControlState.DEFAULT: ft.Colors.LIGHT_BLUE_800,
            ft.ControlState.HOVERED: ft.Colors.LIGHT_BLUE_700,
        },
        padding={
            ft.ControlState.DEFAULT:ft.Padding(top=20, right=20, bottom=20, left=20),
            ft.ControlState.HOVERED:ft.Padding(top=50, right=20, bottom=50, left=20),
        },
        animation_duration=500,
)