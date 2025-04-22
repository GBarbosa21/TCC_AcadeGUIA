from tkinter import Image

import flet as ft
from PIL.ImageOps import expand, cover
from docutils.nodes import image
from docutils.parsers.rst.directives.tables import align
from pygments.styles.dracula import background

from Styles import *

app_bar = ft.AppBar(
        leading=ft.Image(src="assets/favicon.png"),
        leading_width=64,
        title=ft.Text("Acadeguia"),
        center_title=True,
        bgcolor=ft.Colors.LIGHT_BLUE_800,
        color=ft.Colors.BLACK
    )

nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.ARCHIVE, label="Minhas Series"),
            ft.NavigationBarDestination(icon=ft.Icons.FITNESS_CENTER, label="Exercicios"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Exercicios Salvos",
            ),
        ]
    )

container = ft.Container(
    padding= 20,
    alignment= ft.alignment.center,
    width= 800,
    height=600,
    content=ft.Column(
        controls=[
            ft.Image(src="assets/AcadeGUIA.png", expand=True, width=320, height=640, fit=ft.ImageFit.COVER),
            ft.Container(
                width=600,
                height=600,
                alignment=ft.alignment.center,
                content=ft.Column(
                    controls=[
                        ft.ElevatedButton("Treino A", width=200, height=50, on_click=lambda e: print("Treino A")),
                        ft.ElevatedButton("Treino B", width=200, height=50, on_click=lambda e: print("Treino B")),
                        ft.ElevatedButton("Treino C", width=200, height=50, on_click=lambda e: print("Treino C")),
                    ]
                )
            )
        ],
        spacing=30,
        alignment=ft.MainAxisAlignment.CENTER,
    ),
)

btn_exerc_style= ft.ElevatedButton(
    text="Exercicios",
    bgcolor=ft.Colors.LIGHT_BLUE_800,
    color=ft.Colors.BLACK,
    width= 300,
)