import flet as ft
from Styles import EstiloTxt

# =================================================================
# FUNÇÃO DE LAYOUT BASE
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
        controls=[
            # 1. Header
            ft.Container(
                alignment=ft.alignment.center,
                padding=15,
                bgcolor=ft.colors.GREY_900,
                content=ft.Text(
                    titulo, size=24, weight=ft.FontWeight.BOLD, color='#F1F1F1'
                ),
            ),
            # 2. Conteúdo principal
            ft.Container(
                expand=True,
                padding=20,
                content=ft.ListView(
                    expand=True, spacing=20, controls=conteudo
                ),
            ),
            # 3. NavBar
            bottom,
        ]
    )


# =================================================================
# SEUS COMPONENTES
# =================================================================

def botao_menu_principal(texto: str, icone: str, on_click):
    return ft.ElevatedButton(
        content=ft.Row(
            controls=[
                ft.Icon(name=icone, size=22),
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
    routes = ['/exercicios', '/inicio', '/minhas_series']

    def go_route(e):
        page.go(routes[e.control.selected_index])

    return ft.NavigationBar(
        selected_index=selected_index,
        on_change=go_route,
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
                                        on_click=lambda e: on_Save(e) if on_Save else None,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.PLAY_ARROW_OUTLINED,
                                        icon_color='#A6A6F6',
                                        icon_size=32,
                                        tooltip='Play Exercicio',
                                        on_click=lambda e: on_Play(e) if on_Play else None,
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
                                        # CORRIGIDO: Adicionado (e)
                                        on_click=lambda e: on_Delete(e) if on_Delete else None,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.PLAY_ARROW_OUTLINED,
                                        icon_color='#A6A6F6',
                                        icon_size=32,
                                        tooltip='Play Exercicio',
                                        # CORRIGIDO: Adicionado (e)
                                        on_click=lambda e: on_Play(e) if on_Play else None,
                                    )
                                ]
                            ),
                        ]
                    ),
                ],
            )
        )
    )

def btn_inserir_exercicio(on_click=None):
    """Botão para adicionar um novo exercício à série."""
    return ft.ElevatedButton(
        width=350,  # Mesma largura dos cards
        height=70,  # Um pouco menor que o botão de nova série
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREY_900,
            color="#A6A6A6",
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.colors.GREY_800,
            padding=ft.Padding(15, 10, 15, 10),
        ),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.Icon(name=ft.icons.ADD_CIRCLE_OUTLINE, color="#A6A6A6", size=24),
                ft.Text(
                    "Inserir Exercício",
                    size=18,
                    color="#A6A6A6",
                    weight=ft.FontWeight.BOLD
                )
            ]
        )
    )

# --- FUNÇÃO AUXILIAR PARA O CARD SELECIONÁVEL ---
def btn_info_exercicio_salvar(nome_exercicio: str, on_click=None, on_Save=None, on_Play=None) -> ft.Container:
    """Versão simplificada do card de exercício para a tela de seleção."""
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
                                        icon=ft.icons.PLAY_ARROW_OUTLINED,
                                        icon_color='#A6A6F6',
                                        icon_size=32,
                                        tooltip='Play Exercicio',
                                        # CORRIGIDO: Adicionado (e)
                                        on_click=lambda e: on_Play(e) if on_Play else None,
                                    )
                                ]
                            ),
                        ]
                    ),
                ],
            )
        )
    )

def card_exercicio_selecionavel(nome_exercicio: str, on_change_check=None):
    """
    Cria uma linha com um Checkbox e o Card de Exercício ao lado.
    Permite selecionar exercícios para adicionar à série.
    """
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Checkbox(
                on_change=on_change_check,
                fill_color={
                    ft.ControlState.SELECTED: "#A6A6F6",
                    ft.ControlState.DEFAULT: ft.colors.WHITE54
                }
            ),
            # O container expande para o card ocupar o resto da largura
            ft.Container(
                expand=True,
                # Reutilizamos o btn_info_exercicio_salvar definido acima
                content=btn_info_exercicio_salvar(
                    nome_exercicio,
                    on_click=lambda e: print(f"Info de {nome_exercicio}"),
                    on_Play=lambda e: print(f"Play {nome_exercicio}")
                )
            )
        ]
    )