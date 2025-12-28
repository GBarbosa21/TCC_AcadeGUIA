import flet as ft

# Tratamento de importação para rodar de 'src' ou raiz
try:
    from funcoes import layout_com_header_fixado, nav_bar, btn_info_exercicio
    from controllers.catalogo_controller import CatalogoController
    from controllers.exercicios_salvos_controller import ExerciciosSalvosController
except ImportError:
    from src.funcoes import layout_com_header_fixado, nav_bar, btn_info_exercicio
    from src.controllers.catalogo_controller import CatalogoController
    from src.controllers.exercicios_salvos_controller import ExerciciosSalvosController


def exercicio_info(page: ft.Page):
    """View que lista TODOS os exercícios do Catálogo."""

    estado_atual = {"filtro_grupo": None, "busca_texto": None}
    lista_exercicios = ft.Column(spacing=20)

    def carregar_lista():
        lista_exercicios.controls.clear()

        dados = CatalogoController.buscar_filtrado(
            grupo=estado_atual["filtro_grupo"],
            termo=estado_atual["busca_texto"]
        )

        if not dados:
            lista_exercicios.controls.append(
                ft.Container(padding=20, alignment=ft.alignment.center,
                             content=ft.Text("Nenhum exercício encontrado.", color=ft.Colors.GREY_500, size=16))
            )
        else:
            for ex in dados:
                def ir_para_detalhes(e, nome=ex.nome):
                    page.session.set("exercicio_atual", nome)
                    page.go('/detalhes_exercicio')

                def acao_salvar(e, nome=ex.nome):
                    novo_status = ExerciciosSalvosController.alternar_status_favorito(nome)
                    msg = f"{nome} salvo!" if novo_status else f"{nome} removido."
                    page.snack_bar = ft.SnackBar(content=ft.Text(msg, color=ft.Colors.WHITE),
                                                 bgcolor=ft.Colors.GREY_900)
                    page.snack_bar.open = True
                    page.update()

                # --- MUDANÇA AQUI: Passando o grupo muscular ---
                card = btn_info_exercicio(
                    nome_exercicio=ex.nome,
                    grupo_muscular=ex.grupo_muscular,  # <--- ÍCONE DINÂMICO
                    on_click=ir_para_detalhes,
                    on_Play=ir_para_detalhes,
                    on_Save=acao_salvar
                )
                lista_exercicios.controls.append(card)

        page.update()

    # --- Filtros (Lógica Visual) ---
    categorias = ["Perna", "Ombro", "Braço", "Costas", "Peito"]
    botoes_filtro_refs = []

    def filtrar_por_grupo(e):
        btn = e.control
        if estado_atual["filtro_grupo"] == btn.text:
            estado_atual["filtro_grupo"] = None
            btn.style.bgcolor = ft.Colors.GREY_900
            btn.style.color = "#A6A6F6"
            btn.data["selecionado"] = False
        else:
            for b in botoes_filtro_refs:
                b.style.bgcolor = ft.Colors.GREY_900
                b.style.color = "#A6A6F6"
                b.data["selecionado"] = False
            estado_atual["filtro_grupo"] = btn.text
            btn.style.bgcolor = "#A6A6F6"
            btn.style.color = ft.Colors.BLACK
            btn.data["selecionado"] = True
        carregar_lista()

    scroll_filtros = ft.Row(scroll=ft.ScrollMode.HIDDEN, spacing=10)
    for cat in categorias:
        btn = ft.ElevatedButton(
            text=cat,
            data={"selecionado": False},
            style=ft.ButtonStyle(bgcolor=ft.Colors.GREY_900, color="#A6A6F6", shape=ft.RoundedRectangleBorder(radius=8),
                                 padding=ft.Padding(20, 10, 20, 10)),
            on_click=filtrar_por_grupo
        )
        botoes_filtro_refs.append(btn)
        scroll_filtros.controls.append(btn)

    txt_busca = ft.TextField(
        hint_text="Buscar...", expand=True, height=45,
        text_style=ft.TextStyle(size=16), content_padding=ft.Padding(15, 0, 15, 0),
        bgcolor=ft.Colors.GREY_900, border_radius=8,
        on_change=lambda e: atualizar_busca(e.control.value)
    )

    def atualizar_busca(texto):
        estado_atual["busca_texto"] = texto if texto.strip() else None
        carregar_lista()

    def alternar_modo_busca(ativar):
        linha_filtros.visible = not ativar
        linha_busca.visible = ativar
        if ativar:
            txt_busca.focus()
        else:
            txt_busca.value = ""
            estado_atual["busca_texto"] = None
            carregar_lista()
        page.update()

    linha_filtros = ft.Row(
        controls=[ft.Container(content=scroll_filtros, expand=True),
                  ft.IconButton(icon=ft.Icons.SEARCH, icon_color="#A6A6F6", icon_size=28,
                                on_click=lambda e: alternar_modo_busca(True))],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    linha_busca = ft.Row(
        visible=False,
        controls=[txt_busca, ft.IconButton(icon=ft.Icons.CLOSE, icon_color="#A6A6F6", icon_size=28,
                                           on_click=lambda e: alternar_modo_busca(False))],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    carregar_lista()

    return layout_com_header_fixado(
        page, 'Exercícios',
        [ft.Container(content=ft.Column([linha_filtros, linha_busca]), padding=ft.Padding(0, 0, 0, 15)),
         lista_exercicios],
        bottom=nav_bar(page, selected_index=1)
    )