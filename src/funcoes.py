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
            ft.Container(
                width=600,
                height=600,
                alignment=ft.alignment.center,
                content=ft.Column(
                    controls=[
                        ft.Container(
                            margin=ft.Margin(top=20, bottom=20, left=0, right=0),
                            content=ft.Column(
                                controls=[
                                    ft.ElevatedButton("Treino A", width=200, height=60, on_click=lambda e: print("Treino A")),
                                ]
                            )
                        ),
                        ft.Container(
                            margin=ft.Margin(top=20, bottom=20, left=0, right=0),
                            content=ft.Column(
                                controls=[
                                    ft.ElevatedButton("Treino B", width=200, height=60, on_click=lambda e: print("Treino B")),
                                ]
                            )
                        ),
                        ft.Container(
                            margin=ft.Margin(top=20, bottom=20, left=0, right=0),
                            content=ft.Column(
                                controls=[
                                    ft.ElevatedButton("Treino C", width=200, height=60, on_click=lambda e: print("Treino C")),
                                ]
                            )
                        ),
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