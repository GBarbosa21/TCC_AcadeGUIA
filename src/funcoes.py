# funcoes.py
import flet as ft
from Styles import EstiloTxt  # <-- Mantive sua importação original


# =================================================================
# FUNÇÃO DE LAYOUT BASE (A PEÇA QUE FALTAVA)
# =================================================================
def layout_com_header_fixado(
    page: ft.Page, titulo: str, conteudo: list, bottom: ft.NavigationBar
):
    """
    Cria uma View padrão com um header, conteúdo central e a barra de navegação.
    """
    return ft.View(
        route=page.route,
        padding=0,
        controls=[  # MUDANÇA: A barra de navegação agora vai dentro dos 'controls'
            # 1. Header (continua igual)
            ft.Container(
                alignment=ft.alignment.center,
                padding=15,
                bgcolor=ft.colors.GREY_900,
                content=ft.Text(
                    titulo, size=24, weight=ft.FontWeight.BOLD, color='#F1F1F1'
                ),
            ),
            # 2. Conteúdo principal que se expande para empurrar a navbar para baixo
            ft.Container(
                expand=True,  # <-- MUDANÇA CRÍTICA: Faz este container ocupar todo o espaço disponível
                padding=20,
                content=ft.ListView(
                    expand=True, spacing=20, controls=conteudo
                ),
            ),
            # 3. A Barra de Navegação como o último item dos controls
            bottom,
        ]
        # O parâmetro 'bottom' foi removido daqui
    )


# =================================================================
# SEUS COMPONENTES (ORGANIZADOS E SEM DUPLICATAS)
# =================================================================


def botao_menu_principal(texto: str, icone: str, on_click):
    """
    Cria um botão estilizado para o menu principal, conforme o protótipo.
    """
    return ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name=icone, size=22),

                # MUDANÇA: Usando apenas a palavra-chave 'value' para definir o texto.
                # A versão anterior provavelmente tinha 'texto' duas vezes.
                ft.Text(value=texto, size=16, weight=ft.FontWeight.BOLD),

            ],
            spacing=15,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        on_click=on_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=ft.colors.WHITE12,
            color=ft.colors.WHITE,
            padding=ft.padding.all(18),
        ),
        width=320,
        height=65,
    )

def nav_bar(page: ft.Page, selected_index: int) -> ft.NavigationBar:
    """Cria a barra de navegação inferior. Esta é a versão unificada."""
    # MUDANÇA: Ordem das rotas alterada
    routes = ['/exercicios', '/inicio', '/minhas_series']

    def go_route(e):
        page.go(routes[e.control.selected_index])

    return ft.NavigationBar(
        selected_index=selected_index,
        on_change=go_route,
        # MUDANÇA: Ordem dos destinos alterada
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.FITNESS_CENTER, label='Exercícios'
            ),
            ft.NavigationBarDestination(icon=ft.icons.HOME, label='Início'),
            ft.NavigationBarDestination(
                icon=ft.icons.ARCHIVE, label='Minhas Séries'
            ),
        ],
    )


def btn_nova_serie(on_click=None):
    """Botão padrão para criar uma nova série."""
    return ft.ElevatedButton(
        height=100,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREY_900,
            color='#A6A6A6',
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.colors.GREY_800,
            padding=ft.Padding(15, 10, 15, 10),
        ),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.Icon(name=ft.icons.ADD_BOX_OUTLINED, color='#A6A6A6'),
                ft.Text(
                    'Nova Série',
                    size=20,
                    color='#A6A6A6',
                    weight=ft.FontWeight.BOLD,
                ),
            ],
        ),
    )


def criar_card_serie(
    nome: str, qtd_exercicios: int, on_click=None, on_delete=None
):
    """Card para exibir uma série salva."""
    return ft.ElevatedButton(
        width=350,
        height=100,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREY_900,
            color='#F1F1F1',
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.colors.GREY_800,
            padding=ft.Padding(15, 10, 15, 10),
        ),
        on_click=on_click,
        content=ft.Column(
            spacing=5,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(nome, size=24, weight=ft.FontWeight.BOLD),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINE,
                            icon_color=ft.colors.RED_400,
                            tooltip='Excluir série',
                            on_click=lambda e: on_delete()
                            if on_delete
                            else None,
                        ),
                    ],
                ),
                ft.Text(
                    f'{qtd_exercicios} exercícios', size=16, color='#A6A6A6'
                ),
            ],
        ),
    )


def header_editavel(nome_exercicio: str, on_click=None) -> ft.Column:
    """Header usado na página de uma série específica."""
    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=2,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=8,
                controls=[
                    ft.Text(
                        nome_exercicio,
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color='#A6A6F6',
                    ),
                    ft.IconButton(
                        icon=ft.icons.EDIT_OUTLINED,
                        icon_color='#A6A6F6',
                        tooltip='Editar nome da série',
                        on_click=on_click,
                        icon_size=22,
                        style=ft.ButtonStyle(padding=0),
                    ),
                ],
            ),
            ft.Container(height=1, width=200, bgcolor='#A6A6F6'),
        ],
    )


def card_exercicio(
    nome: str, series: int, repeticoes: int, on_click=None
) -> ft.Container:
    """Card para exibir um exercício dentro de uma série."""
    return ft.Container(
        content=ft.ElevatedButton(
            on_click=on_click,
            height=120,
            width=350,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREY_900,
                color='#A6A6F6',
                shape=ft.RoundedRectangleBorder(radius=16),
                padding=ft.Padding(16, 10, 16, 10),
                overlay_color=ft.colors.GREY_800,
            ),
            content=ft.Column(
                spacing=6,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                        controls=[
                            ft.Icon(
                                name=ft.icons.FITNESS_CENTER,
                                color='#A6A6F6',
                                size=32,
                            ),
                            ft.Text(
                                nome,
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color='#A6A6F6',
                                max_lines=2,
                            ),
                        ],
                    ),
                    ft.Container(height=1, bgcolor='#A6A6F6'),
                    ft.Text(
                        f'{series} × {repeticoes}',
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color='#A6A6F6',
                    ),
                ],
            ),
        ),
    )

def btn_info_exercicio(nome_exercicio: str, on_click=None, on_Save=None, on_Play=None) -> ft.Container:
    return ft.Container(
        content=ft.ElevatedButton(
            on_click=on_click,
            height=220,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREY_900,
                color='#A6A6F6',
                shape=ft.RoundedRectangleBorder(radius=16),
                padding=ft.Padding(16, 10, 16, 10),
                overlay_color=ft.colors.GREY_800,
            ),
            content=ft.Column(
                spacing=6,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                        controls=[
                            ft.Icon(
                                name=ft.icons.FITNESS_CENTER,
                                color='#A6A6F6',
                                size=128,
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            ft.Text(
                                f'{nome_exercicio}',
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color='#A6A6F6',
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                spacing=10,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.SAVE_AS,
                                        icon_color='#A6A6F6',
                                        icon_size=32,
                                        tooltip='Salvar Exercicio',
                                        on_click=lambda e: on_Save
                                        if on_Save
                                        else None,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.PLAY_ARROW_OUTLINED,
                                        icon_color='#A6A6F6',
                                        icon_size=32,
                                        tooltip='Play Exercicio',
                                        on_click=lambda e: on_Play
                                        if on_Play
                                        else None,
                                    )
                                ]
                            ),
                        ]
                    ),
                ],
            )
        )
    )

def btn_info_exercicio_salvos(nome_exercicio: str, on_click=None, on_Delete=None, on_Play=None) -> ft.Container:
    return ft.Container(
        content=ft.ElevatedButton(
            on_click=on_click,
            height=220,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREY_900,
                color='#A6A6F6',
                shape=ft.RoundedRectangleBorder(radius=16),
                padding=ft.Padding(16, 10, 16, 10),
                overlay_color=ft.colors.GREY_800,
            ),
            content=ft.Column(
                spacing=6,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                        controls=[
                            ft.Icon(
                                name=ft.icons.FITNESS_CENTER,
                                color='#A6A6F6',
                                size=128,
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            ft.Text(
                                f'{nome_exercicio}',
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color='#A6A6F6',
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                spacing=10,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.SAVE_AS,
                                        icon_color='#A6A6F6',
                                        icon_size=32,
                                        tooltip='Remover Exercicio da lista',
                                        on_click=lambda e: on_Delete
                                        if on_Delete
                                        else None,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.PLAY_ARROW_OUTLINED,
                                        icon_color='#A6A6F6',
                                        icon_size=32,
                                        tooltip='Play Exercicio',
                                        on_click=lambda e: on_Play
                                        if on_Play
                                        else None,
                                    )
                                ]
                            ),
                        ]
                    ),
                ],
            )
        )
    )
