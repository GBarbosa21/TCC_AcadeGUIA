import flet as ft

# Tratamento de importações para rodar de 'src' ou raiz
try:
    from funcoes import layout_com_header_fixado, nav_bar, btn_info_exercicio
    from controllers.catalogo_controller import CatalogoController
    from controllers.exercicio_controller import ExercicioController
except ImportError:
    from src.funcoes import layout_com_header_fixado, nav_bar, btn_info_exercicio
    from src.controllers.catalogo_controller import CatalogoController
    from src.controllers.exercicio_controller import ExercicioController


def selecionar_exercicios(page: ft.Page):
    """View para selecionar múltiplos exercícios e adicionar à série atual."""

    # 1. Recupera o ID da Série atual
    serie_atual_id = page.session.get("serie_atual_id")
    serie_atual_nome = page.session.get("serie_atual_nome") or "Série"

    if not serie_atual_id:
        return ft.View(controls=[ft.Text("Erro: Nenhuma série selecionada. Volte para Minhas Séries.")])

    # 2. Estado
    exercicios_selecionados = set()
    estado_atual = {
        "filtro_grupo": None,
        "busca_texto": None
    }

    # Container da lista
    lista_opcoes = ft.Column(spacing=10)

    # --- Lógica de Seleção ---
    def alternar_selecao(e, nome_exercicio):
        is_selected = e.control.value
        if is_selected:
            exercicios_selecionados.add(nome_exercicio)
        else:
            exercicios_selecionados.discard(nome_exercicio)

        print(f"Selecionados: {len(exercicios_selecionados)}")
        # Não precisa de page.update() aqui pois o checkbox já atualiza visualmente

    # --- Lógica de Carregar Lista (Com Filtros) ---
    def carregar_lista():
        lista_opcoes.controls.clear()

        # Busca no banco filtrado
        dados = CatalogoController.buscar_filtrado(
            grupo=estado_atual["filtro_grupo"],
            termo=estado_atual["busca_texto"]
        )

        if not dados:
            lista_opcoes.controls.append(
                ft.Container(
                    padding=20,
                    alignment=ft.alignment.center,
                    content=ft.Text("Nenhum exercício encontrado.", color=ft.Colors.GREY_500)
                )
            )
        else:
            for ex in dados:
                # Verifica se já estava selecionado para marcar o checkbox
                esta_marcado = ex.nome in exercicios_selecionados

                # Recriamos a linha localmente para poder definir o 'value' do checkbox
                item = ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Checkbox(
                            value=esta_marcado,
                            # Importante: lambda captura o nome correto para cada linha
                            on_change=lambda e, n=ex.nome: alternar_selecao(e, n),
                            fill_color={
                                ft.ControlState.SELECTED: "#A6A6F6",
                                ft.ControlState.DEFAULT: ft.Colors.WHITE54
                            }
                        ),
                        ft.Container(
                            expand=True,
                            content=btn_info_exercicio(
                                nome_exercicio=ex.nome,
                                grupo_muscular=ex.grupo_muscular,  # Passa o grupo para o ícone
                                # Lambdas corrigidos com argumento padrão para evitar bugs de loop
                                on_click=lambda e, n=ex.nome: print(f"Info de {n}"),
                                on_Play=lambda e, n=ex.nome: print(f"Play {n}")
                            )
                        )
                    ]
                )
                lista_opcoes.controls.append(item)

        page.update()

    # --- Filtros e Busca (Igual às outras telas) ---
    categorias = ["Perna", "Ombro", "Braço", "Costas", "Peito"]
    botoes_filtro_refs = []

    def filtrar_por_grupo(e):
        btn = e.control
        grupo = btn.text

        # Reset visual
        for b in botoes_filtro_refs:
            b.style.bgcolor = ft.Colors.GREY_900
            b.style.color = "#A6A6F6"
            b.data["selecionado"] = False

        if estado_atual["filtro_grupo"] == grupo:
            estado_atual["filtro_grupo"] = None  # Desativa
        else:
            estado_atual["filtro_grupo"] = grupo  # Ativa novo
            btn.style.bgcolor = "#A6A6F6"
            btn.style.color = ft.Colors.BLACK
            btn.data["selecionado"] = True

        carregar_lista()

    scroll_filtros = ft.Row(scroll=ft.ScrollMode.HIDDEN, spacing=10)
    for cat in categorias:
        btn = ft.ElevatedButton(
            text=cat, data={"selecionado": False},
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
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    linha_busca = ft.Row(
        visible=False,
        controls=[
            txt_busca,
            ft.IconButton(icon=ft.Icons.CLOSE, icon_color="#A6A6F6", icon_size=28,
                          on_click=lambda e: alternar_modo_busca(False))
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # --- Lógica de Salvar ---
    def adicionar_a_serie(e):
        if not exercicios_selecionados:
            page.snack_bar = ft.SnackBar(content=ft.Text("Selecione pelo menos um exercício!"))
            page.snack_bar.open = True
            page.update()
            return

        quantidade = 0
        try:
            for nome_ex in exercicios_selecionados:
                # 1. Busca o exercício no catálogo para obter o grupo muscular correto
                ex_catalogo = CatalogoController.buscar_por_nome(nome_ex)
                grupo = ex_catalogo.grupo_muscular if ex_catalogo else "Geral"

                # 2. Cria o exercício na série passando o grupo
                ExercicioController.criar(
                    nome=nome_ex,
                    serie_id=serie_atual_id,
                    grupo_muscular=grupo,  # <--- Importante para o ícone aparecer na série
                    series_reps="4x12"
                )
                quantidade += 1

            page.go('/serie')
            page.snack_bar = ft.SnackBar(content=ft.Text(f"{quantidade} exercícios adicionados!"),
                                         bgcolor=ft.Colors.GREEN)
            page.snack_bar.open = True
            page.update()

        except Exception as erro:
            print(f"Erro: {erro}")
            page.snack_bar = ft.SnackBar(content=ft.Text("Erro ao adicionar."), bgcolor=ft.Colors.RED)
            page.snack_bar.open = True
            page.update()

    # Inicializa a lista
    carregar_lista()

    # --- Montagem da Tela ---
    conteudo = [
        # Título
        ft.Container(
            padding=5,
            content=ft.Text(f"Adicionar a: {serie_atual_nome}", size=16, color=ft.Colors.GREY_400)
        ),
        # Filtros
        ft.Container(
            content=ft.Column([linha_padrao, linha_busca]),
            padding=ft.Padding(0, 0, 0, 10)
        ),
        # Lista
        lista_opcoes,
        # Espaço extra no final para o botão flutuante não cobrir o último item
        ft.Container(height=80)
    ]

    # Cria a View Base
    view = layout_com_header_fixado(
        page,
        'Selecionar Exercícios',
        conteudo,
        bottom=nav_bar(page, selected_index=2),
    )

    # Adiciona o Botão Flutuante (FAB) à View
    view.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.CHECK,
        text="Finalizar",
        bgcolor="#A6A6F6",
        content=ft.Row(
            [ft.Icon(ft.Icons.CHECK, color=ft.Colors.BLACK),
             ft.Text("Finalizar", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5
        ),
        width=140,
        on_click=adicionar_a_serie,
    )

    return view