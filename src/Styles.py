import flet as ft

btn_exerc_style= ft.ButtonStyle(
        color={
            ft.ControlState.DEFAULT: ft.Colors.LIGHT_BLUE_800,
            ft.ControlState.HOVERED: ft.Colors.LIGHT_BLUE_700,
        },
        padding={
            ft.ControlState.DEFAULT: 10,
            ft.ControlState.HOVERED: 15,
        },
        animation_duration=500,
)