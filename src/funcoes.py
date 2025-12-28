import flet as ft

# Tratamento de importação apenas para Styles
try:
    from Styles import EstiloTxt
except ImportError:
    try:
        from src.Styles import EstiloTxt
    except ImportError:
        EstiloTxt = ft.TextStyle(size=16)


# =================================================================
# MAPA DE IMAGENS POR GRUPO MUSCULAR (NOVO)
# =================================================================
def obter_imagem_por_grupo(grupo):
    """
    Retorna o caminho da imagem (na pasta assets) baseado no grupo muscular.
    Certifique-se de ter os arquivos .png correspondentes na pasta assets.
    """
    if not grupo:
        return "padrao.png"  # Imagem genérica se não tiver grupo

    g = str(grupo).lower()

    if "peito" in g:
        return "peito.png"
    elif "perna" in g or "quadriceps" in g or "gluteo" in g:
        return "perna.png"
    elif "braço" in g or "biceps" in g or "triceps" in g:
        return "braco.png"
    elif "costas" in g or "dorsal" in g:
        return "costas.png"
    elif "ombro" in g or "deltoide" in g:
        return "ombro.png"
    else:
        return "padrao.png"


# =================================================================
# FUNÇÃO DE LAYOUT BASE
# =================================================================
def layout_com_header_fixado(
        page: ft.Page, titulo: str, conteudo: list, bottom: ft.NavigationBar
):
    return ft.View(
        route=page.route,
        padding=0,
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                padding=15,
                bgcolor=ft.Colors.GREY_900,
                content=ft.Text(
                    titulo, size=24, weight=ft.FontWeight.BOLD, color='#F1F1F1'
                ),
            ),
            ft.Container(
                expand=True,
                padding=20,
                content=ft.ListView(
                    expand=True, spacing=20, controls=conteudo
                ),
            ),
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
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        on_click=on_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=ft.Colors.WHITE12,
            color=ft.Colors.WHITE,
            padding=ft.padding.all(18),
        ),
        height=65,
    )


def nav_bar(page: ft.Page, selected_index: int) -> ft.NavigationBar:
    routes = ['/exercicios', '/inicio', '/minhas_series']

    def go_route(e): page.go(routes[e.control.selected_index])

    return ft.NavigationBar(
        selected_index=selected_index,
        on_change=go_route,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.FITNESS_CENTER, label='Exercícios'),
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label='Início'),
            ft.NavigationBarDestination(icon=ft.Icons.ARCHIVE, label='Minhas Séries'),
        ],
    )


def btn_nova_serie(on_click=None):
    return ft.ElevatedButton(
        height=100,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREY_900,
            color='#A6A6A6',
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.Colors.GREY_800,
            padding=ft.Padding(15, 10, 15, 10),
        ),
        on_click=on_click,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.Icon(name=ft.Icons.ADD_BOX_OUTLINED, color='#A6A6A6'),
                ft.Text('Nova Série', size=20, color='#A6A6A6', weight=ft.FontWeight.BOLD),
            ],
        ),
    )


def criar_card_serie(nome: str, qtd_exercicios: int, on_click=None, on_delete=None):
    return ft.ElevatedButton(
        height=100,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREY_900,
            color='#F1F1F1',
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
                        ft.Text(nome, size=24, weight=ft.FontWeight.BOLD),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            icon_color=ft.Colors.RED_400,
                            tooltip='Excluir série',
                            on_click=lambda e: on_delete() if on_delete else None,
                        ),
                    ],
                ),
                ft.Text(f'{qtd_exercicios} exercícios', size=16, color='#A6A6A6'),
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
                    ft.Text(nome_exercicio, size=32, weight=ft.FontWeight.BOLD, color='#A6A6F6'),
                    ft.IconButton(
                        icon=ft.Icons.EDIT_OUTLINED,
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
        nome: str, series: int, repeticoes: int, on_click=None, on_edit=None, grupo_muscular="Geral"
) -> ft.Container:
    """Card para exibir um exercício dentro de uma série."""

    # 1. Busca a IMAGEM dinâmica
    imagem_src = obter_imagem_por_grupo(grupo_muscular)

    linha_inferior = [
        ft.Text(f'{series} × {repeticoes}', size=20, weight=ft.FontWeight.BOLD, color='#A6A6F6')
    ]
    if on_edit:
        linha_inferior.append(
            ft.IconButton(icon=ft.Icons.EDIT, icon_color="#A6A6F6", icon_size=20, tooltip="Editar", on_click=on_edit)
        )

    return ft.Container(
        content=ft.ElevatedButton(
            on_click=on_click,
            height=120,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.GREY_900,
                color='#A6A6F6',
                shape=ft.RoundedRectangleBorder(radius=16),
                padding=ft.Padding(16, 10, 16, 10),
                overlay_color=ft.Colors.GREY_800,
            ),
            content=ft.Column(
                spacing=6,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=15,
                        controls=[
                            # MUDANÇA: Removido color="..." para manter cores originais
                            ft.Image(
                                src=imagem_src,
                                width=40,
                                height=40,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text(
                                nome,
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color='#A6A6F6',
                                max_lines=2,
                                expand=True,
                                overflow=ft.TextOverflow.ELLIPSIS
                            ),
                        ],
                    ),
                    ft.Container(height=1, bgcolor='#A6A6F6'),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=linha_inferior
                    ),
                ],
            ),
        ),
    )


def btn_info_exercicio(nome_exercicio: str, on_click=None, on_Save=None, on_Play=None,
                       grupo_muscular="Geral") -> ft.Container:
    imagem_src = obter_imagem_por_grupo(grupo_muscular)

    return ft.Container(
        content=ft.ElevatedButton(
            on_click=on_click,
            height=220,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.GREY_900,
                color='#A6A6F6',
                shape=ft.RoundedRectangleBorder(radius=16),
                padding=ft.Padding(16, 10, 16, 10),
                overlay_color=ft.Colors.GREY_800,
            ),
            content=ft.Column(
                spacing=6,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                        controls=[
                            # Imagem Grande no Card - Removido color="..."
                            ft.Image(
                                src=imagem_src,
                                width=100,
                                height=100,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            ft.Text(f'{nome_exercicio}', size=20, weight=ft.FontWeight.BOLD, color='#A6A6F6',
                                    expand=True, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS)
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                spacing=10,
                                controls=[
                                    ft.IconButton(icon=ft.Icons.SAVE_AS, icon_color='#A6A6F6', icon_size=32,
                                                  on_click=lambda e: on_Save(e) if on_Save else None),
                                    ft.IconButton(icon=ft.Icons.PLAY_ARROW_OUTLINED, icon_color='#A6A6F6', icon_size=32,
                                                  on_click=lambda e: on_Play(e) if on_Play else None)
                                ]
                            ),
                        ]
                    ),
                ],
            )
        )
    )


def btn_info_exercicio_salvos(nome_exercicio: str, on_click=None, on_Delete=None, on_Play=None,
                              grupo_muscular="Geral") -> ft.Container:
    imagem_src = obter_imagem_por_grupo(grupo_muscular)

    return ft.Container(
        content=ft.ElevatedButton(
            on_click=on_click,
            height=220,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.GREY_900,
                color='#A6A6F6',
                shape=ft.RoundedRectangleBorder(radius=16),
                padding=ft.Padding(16, 10, 16, 10),
                overlay_color=ft.Colors.GREY_800,
            ),
            content=ft.Column(
                spacing=6,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                        controls=[
                            # Imagem Grande no Card - Removido color="..."
                            ft.Image(
                                src=imagem_src,
                                width=100,
                                height=100,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            ft.Text(f'{nome_exercicio}', size=20, weight=ft.FontWeight.BOLD, color='#A6A6F6',
                                    expand=True, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS)
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                spacing=10,
                                controls=[
                                    ft.IconButton(icon=ft.Icons.SAVE_AS, icon_color='#A6A6F6', icon_size=32,
                                                  tooltip='Remover',
                                                  on_click=lambda e: on_Delete(e) if on_Delete else None),
                                    ft.IconButton(icon=ft.Icons.PLAY_ARROW_OUTLINED, icon_color='#A6A6F6', icon_size=32,
                                                  on_click=lambda e: on_Play(e) if on_Play else None)
                                ]
                            ),
                        ]
                    ),
                ],
            )
        )
    )


def btn_inserir_exercicio(on_click=None):
    return ft.ElevatedButton(
        height=70,
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
                ft.Icon(name=ft.Icons.ADD_CIRCLE_OUTLINE, color="#A6A6A6", size=24),
                ft.Text("Inserir Exercício", size=18, color="#A6A6A6", weight=ft.FontWeight.BOLD)
            ]
        )
    )


def card_exercicio_selecionavel(nome_exercicio: str, on_change_check=None, grupo_muscular="Geral"):
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Checkbox(
                on_change=on_change_check,
                fill_color={
                    ft.ControlState.SELECTED: "#A6A6F6",
                    ft.ControlState.DEFAULT: ft.Colors.WHITE54
                }
            ),
            ft.Container(
                expand=True,
                content=btn_info_exercicio(
                    nome_exercicio,
                    grupo_muscular=grupo_muscular,
                    on_click=lambda e: print(f"Info de {nome_exercicio}"),
                    on_Play=lambda e: print(f"Play {nome_exercicio}")
                )
            )
        ]
    )