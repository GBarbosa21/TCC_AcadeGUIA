import flet as ft
from setuptools.command.alias import alias
from Styles import *

app_bar = ft.AppBar(
    leading=ft.Image(src='assets/favicon.png'),
    leading_width=64,
    title=ft.Text('Acadeguia'),
    center_title=True,
    bgcolor=ft.Colors.LIGHT_BLUE_800,
    color=ft.Colors.BLACK,
)

nav_bar = ft.NavigationBar(
    destinations=[
        ft.NavigationBarDestination(
            icon=ft.Icons.ARCHIVE, label='Minhas Series'
        ),
        ft.NavigationBarDestination(
            icon=ft.Icons.HOME,
            label='Início',
        ),
        ft.NavigationBarDestination(
            icon=ft.Icons.FITNESS_CENTER, label='Exercicios'
        ),
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
                    src='assets/AcadeGUIA.png',
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
                            'Menu Principal',
                            style=EstiloTxt,
                            text_align=ft.TextAlign.CENTER,  # 👈 centraliza o texto
                        ),
                        ft.ElevatedButton(
                            'Minhas Séries',
                            width=500,  # 👈 botão maior para telas grandes
                            height=60,
                            icon=ft.Icons.ARCHIVE,
                            on_click=lambda e: e.page.go("/minhas_series")
                        ),
                        ft.ElevatedButton(
                            'Exercícios',
                            width=500,
                            height=60,
                            icon=ft.Icons.FITNESS_CENTER,
                            on_click=lambda e: print('Treino B'),
                        ),
                        ft.ElevatedButton(
                            'Exercícios Salvos',
                            width=500,
                            height=60,
                            icon=ft.Icons.BOOKMARK_BORDER,
                            on_click=lambda e: print('Treino C'),
                        ),
                    ],
                ),
            ),
        ],
    ),
)


def header_texto(texto: str) -> ft.Container:
    return ft.Container(
        alignment=ft.alignment.top_center,
        padding=ft.Padding(0, 30, 0, 10),  # (left, top, right, bottom)
        content=ft.Text(
            texto,
            size=28,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
            color="#F1F1F1"
        )
    )

def botao_nova_serie(on_click_fn):
    return ft.Container(
        alignment=ft.alignment.center,
        padding=ft.Padding(20, 10, 20, 10),
        content=ft.ElevatedButton(
            text="Nova série",
            icon=ft.icons.ADD_BOX_OUTLINED,
            width=300,  # 👈 largura mais destacada
            height=50,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
            ),
            on_click=on_click_fn
        )
    )

def layout_com_header_fixado(titulo: str, conteudo: list[ft.Control], nav_bar: ft.NavigationBar):
    return ft.View(
            route=f"/{titulo.lower().replace(' ', '_')}",
            controls=[
                ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        # Título fixo
                        ft.Container(
                            alignment=ft.alignment.top_center,
                            padding=ft.Padding(0, 20, 0, 10),
                            content=ft.Text(
                                titulo,
                                size=28,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.WHITE
                            )
                        ),
                        # Conteúdo que cresce e rola
                        ft.Container(
                            expand=True,
                            content=ft.ListView(
                                expand=True,
                                spacing=10,
                                padding=20,
                                controls=conteudo
                            )
                        ),
                        # NAVIGATION BAR no fim (simulada)
                        nav_bar
                    ]
                )
            ]
        )

def criar_card_serie(nome: str, qtd_exercicios: int, on_click=None, on_delete=None):
    return ft.ElevatedButton(
        width=300,
        height=100,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREY_900,
            color="#F1F1F1",
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.Colors.GREY_800,
            padding=ft.Padding(15, 10, 15, 10),
        ),
        on_click=on_click,
        content=ft.Column(
            spacing=5,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(nome, size=35, weight=ft.FontWeight.BOLD, theme_style=ft.TextThemeStyle.DISPLAY_LARGE),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINE,
                            icon_color=ft.Colors.RED_300,
                            tooltip="Excluir série",
                            on_click=lambda e: on_delete() if on_delete else None
                        )
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.Text(f"{qtd_exercicios} exercícios", size=24, color="#A6A6A6", text_align=ft.TextAlign.RIGHT)
                    ]
                )
            ]
        )
    )

def btn_nova_serie(on_click=None):
    return ft.ElevatedButton(
        height=100,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREY_900,
            color="#A6A6A6",
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.Colors.GREY_800,
            padding=ft.Padding(15, 10, 15, 10),
        ),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.Icon(name=ft.icons.ADD_BOX_OUTLINED, color="#A6A6A6"),
                ft.Text("Nova Série", size=20, color="#A6A6A6", weight=ft.FontWeight.BOLD)
            ]
        )
    )