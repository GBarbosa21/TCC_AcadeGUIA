# serie.py
import flet as ft
from ..funcoes import layout_com_header_fixado, nav_bar, btn_info_exercicio_salvos


def exercicios_salvos_info(page: ft.Page):
    """View que lista os exercícios salvos pelo usuário."""

    # --- 1. Lógica dos Filtros ---

    categorias = ["Perna", "Ombro", "Braço", "Costas", "Peito"]

    def criar_botao_filtro(texto):
        def alternar_filtro(e):
            btn = e.control
            esta_selecionado = btn.data.get("selecionado", False)

            if esta_selecionado:
                btn.style.bgcolor = ft.colors.GREY_900
                btn.style.color = "#A6A6F6"
                btn.data["selecionado"] = False
            else:
                btn.style.bgcolor = "#A6A6F6"
                btn.style.color = ft.colors.BLACK
                btn.data["selecionado"] = True

            btn.update()
            print(f"Filtro '{texto}' alterado")

        return ft.ElevatedButton(
            text=texto,
            data={"selecionado": False},
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREY_900,
                color="#A6A6F6",
                shape=ft.RoundedRectangleBorder(radius=8),
                padding=ft.Padding(20, 10, 20, 10),
            ),
            on_click=alternar_filtro
        )

    scroll_filtros = ft.Row(
        controls=[criar_botao_filtro(cat) for cat in categorias],
        scroll=ft.ScrollMode.HIDDEN,
        spacing=10
    )

    # --- 2. Lógica da Busca (Campo de Texto) ---

    # Campo de texto para digitar o nome
    txt_busca = ft.TextField(
        hint_text="Buscar exercício...",
        expand=True,
        height=45,
        text_style=ft.TextStyle(size=16),
        content_padding=ft.Padding(15, 0, 15, 0),
        bgcolor=ft.colors.GREY_900,
        border_radius=8,
        # Ação ao digitar (aqui você filtraria a lista real)
        on_change=lambda e: print(f"Digitando busca: {e.control.value}")
    )

    # Função para alternar entre os modos (Filtros <-> Busca)
    def alternar_modo_busca(ativar):
        linha_padrao.visible = not ativar
        linha_busca.visible = ativar

        if ativar:
            txt_busca.focus()  # Foca no texto automaticamente
        else:
            txt_busca.value = ""  # Limpa ao fechar

        page.update()

    # Modo 1: Linha Padrão (Filtros + Ícone Lupa)
    linha_padrao = ft.Row(
        controls=[
            ft.Container(content=scroll_filtros, expand=True),
            ft.IconButton(
                icon=ft.Icons.SEARCH,
                icon_color="#A6A6F6",
                icon_size=28,
                tooltip="Buscar por nome",
                on_click=lambda e: alternar_modo_busca(True)  # Ativa busca
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Modo 2: Linha de Busca (Campo de Texto + Ícone Fechar)
    linha_busca = ft.Row(
        visible=False,  # Começa invisível
        controls=[
            txt_busca,
            ft.IconButton(
                icon=ft.Icons.CLOSE,
                icon_color="#A6A6F6",
                icon_size=28,
                tooltip="Cancelar busca",
                on_click=lambda e: alternar_modo_busca(False)  # Desativa busca
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # --- 3. Lista de Exercícios ---

    lista_exercicios = ft.Column(spacing=20)

    def remover_exercicio(controle_pai):
        lista_exercicios.controls.remove(controle_pai)
        page.update()
        print("Exercício removido dos salvos!")

    def criar_item_salvo(nome):
        item = None

        def on_delete_click(e):
            remover_exercicio(item)

        item = btn_info_exercicio_salvos(
            nome_exercicio=nome,
            on_click=lambda e: print(f"Abrir detalhes de {nome}"),
            on_Delete=on_delete_click,
            on_Play=lambda e: print(f"Play em {nome}")
        )
        return item

    lista_exercicios.controls.extend([
        criar_item_salvo('Supino Reto'),
        criar_item_salvo('Agachamento Livre'),
        criar_item_salvo('Desenvolvimento Halteres'),
    ])

    # Montagem do Conteúdo da Página
    conteudo = [
        # O topo agora contém as duas linhas (uma visível por vez)
        ft.Container(
            content=ft.Column([linha_padrao, linha_busca]),
            padding=ft.Padding(0, 0, 0, 15)
        ),
        lista_exercicios
    ]

    return layout_com_header_fixado(
        page,
        'Exercícios Salvos',
        conteudo,
        bottom=nav_bar(page, selected_index=0),
    )