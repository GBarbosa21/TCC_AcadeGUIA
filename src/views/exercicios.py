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
    """View que lista TODOS os exercícios do Catálogo (Banco de Dados)."""

    # --- Variáveis de Estado ---
    estado_atual = {
        "filtro_grupo": None,
        "busca_texto": None
    }

    lista_exercicios = ft.Column(spacing=20)

    # --- Função Principal: Carregar Lista do Catálogo ---
    def carregar_lista():
        lista_exercicios.controls.clear()

        # Busca no banco usando os filtros atuais
        dados = CatalogoController.buscar_filtrado(
            grupo=estado_atual["filtro_grupo"],
            termo=estado_atual["busca_texto"]
        )

        if not dados:
            lista_exercicios.controls.append(
                ft.Container(
                    padding=20,
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        "Nenhum exercício encontrado.",
                        color=ft.colors.GREY_500,
                        size=16
                    )
                )
            )
        else:
            for ex in dados:
                # 1. Navegação para Detalhes
                def ir_para_detalhes(e, nome=ex.nome):
                    print(f"Navegando para detalhes de: {nome}")
                    page.session.set("exercicio_atual", nome)
                    page.go('/detalhes_exercicio')

                # 2. Ação de Salvar nos Favoritos
                def acao_salvar(e, nome=ex.nome):
                    print(f"Tentando salvar/remover favorito: {nome}")

                    # Tenta alternar o status no banco
                    novo_status = ExerciciosSalvosController.alternar_status_favorito(nome)

                    # Verifica o resultado
                    if novo_status is True:
                        texto_msg = f"{nome} salvo nos favoritos!"
                        cor_msg = ft.colors.GREEN
                    elif novo_status is False:
                        # Pode ser removido ou erro. Se o banco estiver sem a coluna, vai cair aqui.
                        texto_msg = f"{nome} removido dos favoritos (ou erro ao salvar)."
                        cor_msg = ft.colors.RED

                    print(f"Resultado da ação: {texto_msg}")

                    page.snack_bar = ft.SnackBar(content=ft.Text(texto_msg, color=ft.colors.WHITE),
                                                 bgcolor=ft.colors.GREY_900)
                    page.snack_bar.open = True
                    page.update()

                # Cria o card usando o componente visual padrão (com disquete)
                card = btn_info_exercicio(
                    nome_exercicio=ex.nome,
                    on_click=ir_para_detalhes,
                    on_Play=ir_para_detalhes,
                    on_Save=acao_salvar  # Conecta a lógica de salvar
                )
                lista_exercicios.controls.append(card)

        page.update()

    # --- Lógica de Filtros (Categorias) ---
    categorias = ["Perna", "Ombro", "Braço", "Costas", "Peito"]
    botoes_filtro_refs = []

    def filtrar_por_grupo(e):
        btn = e.control
        grupo_clicado = btn.text

        # Verifica se já estava selecionado para permitir desmarcar (toggle)
        ja_estava_selecionado = (estado_atual["filtro_grupo"] == grupo_clicado)

        # Reseta visualmente todos os botões
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
            text=cat,
            data={"selecionado": False},
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREY_900,
                color="#A6A6F6",
                shape=ft.RoundedRectangleBorder(radius=8),
                padding=ft.Padding(20, 10, 20, 10),
            ),
            on_click=filtrar_por_grupo
        )
        botoes_filtro_refs.append(btn)
        scroll_filtros.controls.append(btn)

    # --- Lógica de Busca (Texto) ---
    txt_busca = ft.TextField(
        hint_text="Buscar exercício...",
        expand=True,
        height=45,
        text_style=ft.TextStyle(size=16),
        content_padding=ft.Padding(15, 0, 15, 0),
        bgcolor=ft.colors.GREY_900,
        border_radius=8,
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

    # Layout do Topo: Alterna entre Filtros e Campo de Busca
    linha_padrao = ft.Row(
        controls=[
            ft.Container(content=scroll_filtros, expand=True),
            ft.IconButton(
                icon=ft.Icons.SEARCH,
                icon_color="#A6A6F6",
                icon_size=28,
                tooltip="Buscar por nome",
                on_click=lambda e: alternar_modo_busca(True)
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    linha_busca = ft.Row(
        visible=False,
        controls=[
            txt_busca,
            ft.IconButton(
                icon=ft.Icons.CLOSE,
                icon_color="#A6A6F6",
                icon_size=28,
                tooltip="Cancelar busca",
                on_click=lambda e: alternar_modo_busca(False)
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # --- Inicialização ---
    carregar_lista()

    # --- Montagem da Tela ---
    conteudo = [
        ft.Container(
            content=ft.Column([linha_padrao, linha_busca]),
            padding=ft.Padding(0, 0, 0, 15)
        ),
        lista_exercicios
    ]

    return layout_com_header_fixado(
        page,
        'Exercícios',
        conteudo,
        bottom=nav_bar(page, selected_index=1),  # Índice 1 = Exercícios
    )