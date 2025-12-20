import flet as ft

# Tratamento de importação para rodar de 'src' ou raiz
try:
    from funcoes import layout_com_header_fixado, nav_bar, btn_info_exercicio_salvos
    from controllers.exercicios_salvos_controller import ExerciciosSalvosController
except ImportError:
    from src.funcoes import layout_com_header_fixado, nav_bar, btn_info_exercicio_salvos
    from src.controllers.exercicios_salvos_controller import ExerciciosSalvosController


def exercicios_salvos_info(page: ft.Page):
    """View que lista APENAS os exercícios salvos (favoritos)."""

    estado_atual = {
        "filtro_grupo": None,
        "busca_texto": None
    }

    lista_exercicios = ft.Column(spacing=20)

    # --- Função Principal: Carregar Lista de Favoritos ---
    def carregar_lista():
        lista_exercicios.controls.clear()

        # USA O NOVO CONTROLLER: Busca apenas onde favorito=True
        dados = ExerciciosSalvosController.buscar_apenas_salvos(
            grupo=estado_atual["filtro_grupo"],
            termo=estado_atual["busca_texto"]
        )

        if not dados:
            lista_exercicios.controls.append(
                ft.Container(
                    padding=40,
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        "Nenhum exercício salvo ainda.\nVá na aba 'Exercícios' e clique no ícone de salvar para adicionar!",
                        color=ft.colors.GREY_500,
                        size=16,
                        text_align=ft.TextAlign.CENTER
                    )
                )
            )
        else:
            for ex in dados:
                def ir_para_detalhes(e, nome=ex.nome):
                    page.session.set("exercicio_atual", nome)
                    page.go('/detalhes_exercicio')

                def remover_favorito(e, nome=ex.nome):
                    # Remove e atualiza a tela
                    ExerciciosSalvosController.alternar_status_favorito(nome)
                    carregar_lista()

                    page.snack_bar = ft.SnackBar(content=ft.Text(f"{nome} removido dos salvos!"))
                    page.snack_bar.open = True
                    page.update()

                # Usa o componente visual 'salvos' (que tem ícone de remover/disquete)
                card = btn_info_exercicio_salvos(
                    nome_exercicio=ex.nome,
                    on_click=ir_para_detalhes,
                    on_Play=ir_para_detalhes,
                    on_Delete=remover_favorito  # Botão de ação (remover)
                )
                lista_exercicios.controls.append(card)

        page.update()

    # --- Lógica de Filtros (Igual à tela de exercícios) ---
    categorias = ["Perna", "Ombro", "Braço", "Costas", "Peito"]
    botoes_filtro_refs = []

    def filtrar_por_grupo(e):
        btn = e.control
        grupo_clicado = btn.text
        ja_estava_selecionado = (estado_atual["filtro_grupo"] == grupo_clicado)

        for b in botoes_filtro_refs:
            b.style.bgcolor = ft.colors.GREY_900
            b.style.color = "#A6A6F6"
            b.data["selecionado"] = False

        if ja_estava_selecionado:
            estado_atual["filtro_grupo"] = None
        else:
            estado_atual["filtro_grupo"] = grupo_clicado
            btn.style.bgcolor = "#A6A6F6"
            btn.style.color = ft.colors.BLACK
            btn.data["selecionado"] = True

        carregar_lista()

    scroll_filtros = ft.Row(scroll=ft.ScrollMode.HIDDEN, spacing=10)
    for cat in categorias:
        btn = ft.ElevatedButton(
            text=cat, data={"selecionado": False},
            style=ft.ButtonStyle(bgcolor=ft.colors.GREY_900, color="#A6A6F6", shape=ft.RoundedRectangleBorder(radius=8),
                                 padding=ft.Padding(20, 10, 20, 10)),
            on_click=filtrar_por_grupo
        )
        botoes_filtro_refs.append(btn)
        scroll_filtros.controls.append(btn)

    # --- Lógica de Busca ---
    txt_busca = ft.TextField(
        hint_text="Buscar nos salvos...",
        expand=True, height=45, text_style=ft.TextStyle(size=16),
        content_padding=ft.Padding(15, 0, 15, 0), bgcolor=ft.colors.GREY_900, border_radius=8,
        on_change=lambda e: atualizar_busca(e.control.value)
    )

    def atualizar_busca(texto):
        estado_atual["busca_texto"] = texto if texto.strip() else None
        carregar_lista()

    def alternar_modo_busca(ativar):
        linha_padrao.visible = not ativar
        linha_busca.visible = ativar
        if ativar:
            txt_busca.focus()
        else:
            txt_busca.value = ""
            estado_atual["busca_texto"] = None
            carregar_lista()
        page.update()

    linha_padrao = ft.Row(
        controls=[
            ft.Container(content=scroll_filtros, expand=True),
            ft.IconButton(icon=ft.Icons.SEARCH, icon_color="#A6A6F6", icon_size=28,
                          on_click=lambda e: alternar_modo_busca(True))
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    linha_busca = ft.Row(
        visible=False,
        controls=[
            txt_busca,
            ft.IconButton(icon=ft.Icons.CLOSE, icon_color="#A6A6F6", icon_size=28,
                          on_click=lambda e: alternar_modo_busca(False))
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    carregar_lista()

    conteudo = [
        ft.Container(content=ft.Column([linha_padrao, linha_busca]), padding=ft.Padding(0, 0, 0, 15)),
        lista_exercicios
    ]

    return layout_com_header_fixado(
        page, 'Exercícios Salvos', conteudo, bottom=nav_bar(page, selected_index=0)
    )