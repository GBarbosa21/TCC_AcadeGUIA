import flet as ft
from setuptools.command.alias import alias

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
        ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início", ),
        ft.NavigationBarDestination(icon=ft.Icons.FITNESS_CENTER, label="Exercicios"),
    ]
)

container = ft.Container(
    expand=True,  # 👈 ocupa toda a tela disponível
    padding=20,
    alignment=ft.alignment.center,
    content=ft.Column(
        spacing=30,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                expand=True,
                height=200,
                padding=ft.Padding(20, 0, 20, 0),
                content=ft.Image(
                    src="assets/AcadeGUIA.png",
                    fit=ft.ImageFit.FIT_WIDTH,  # 👈 imagem se ajusta à largura
                ),
            ),
            ft.Container(
                alignment=ft.alignment.center,
                expand=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    controls=[
                        ft.Text(
                            "Menu Principal",
                            style=EstiloTxt,
                            text_align=ft.TextAlign.CENTER,  # 👈 centraliza o texto
                        ),
                        ft.ElevatedButton(
                            "Minhas Séries",
                            width=500,  # 👈 botão maior para telas grandes
                            height=60,
                            icon=ft.Icons.ARCHIVE,
                            on_click=lambda e: e.page.go("/minhas_series"),
                        ),
                        ft.ElevatedButton(
                            "Exercícios",
                            width=500,
                            height=60,
                            icon=ft.Icons.FITNESS_CENTER,
                            on_click=lambda e: print("Treino B")
                        ),
                        ft.ElevatedButton(
                            "Exercícios Salvos",
                            width=500,
                            height=60,
                            icon=ft.Icons.BOOKMARK_BORDER,
                            on_click=lambda e: print("Treino C")
                        ),
                    ]
                ),
            ),
        ]
    )
)
