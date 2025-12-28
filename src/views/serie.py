import flet as ft

# Tratamento de importação para rodar de 'src' ou raiz
try:
    from funcoes import layout_com_header_fixado, nav_bar, card_exercicio, btn_inserir_exercicio
    from controllers.exercicio_controller import ExercicioController
except ImportError:
    from src.funcoes import layout_com_header_fixado, nav_bar, card_exercicio, btn_inserir_exercicio
    from src.controllers.exercicio_controller import ExercicioController


def serie(page: ft.Page):
    """View dinâmica que lista exercícios de uma série específica."""

    # 1. Recupera dados da sessão
    serie_id = page.session.get("serie_atual_id")
    serie_nome = page.session.get("serie_atual_nome") or "Série"

    if not serie_id:
        return ft.View(controls=[ft.Text("Erro: Nenhuma série selecionada. Volte para o início.")])

    # --- Container Dinâmico (Full Width) ---
    # STRETCH faz os filhos (cards sem largura fixa) ocuparem toda a tela
    container_exercicios = ft.Column(
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH
    )

    # --- Lógica de Edição (Dialog) ---
    txt_series = ft.TextField(label="Séries", width=100, keyboard_type=ft.KeyboardType.NUMBER)
    txt_reps = ft.TextField(label="Repetições", width=100, keyboard_type=ft.KeyboardType.NUMBER)
    # Variável para guardar qual ID estamos a editar no momento
    exercicio_em_edicao_id = [None]

    def fechar_dialogo_edicao(e):
        page.close(dialog_edicao)

    def salvar_edicao(e):
        id_ex = exercicio_em_edicao_id[0]
        novas_series = txt_series.value
        novas_reps = txt_reps.value

        if id_ex and novas_series and novas_reps:
            novo_valor = f"{novas_series}x{novas_reps}"
            ExercicioController.atualizar(id_ex, novo_valor)
            page.close(dialog_edicao)
            carregar_conteudo()  # Recarrega a tela
            page.snack_bar = ft.SnackBar(content=ft.Text("Atualizado!"), bgcolor=ft.Colors.GREEN)
            page.snack_bar.open = True
            page.update()

    dialog_edicao = ft.AlertDialog(
        title=ft.Text("Editar Série"),
        content=ft.Row([txt_series, ft.Text("x", size=20), txt_reps], alignment=ft.MainAxisAlignment.CENTER),
        actions=[
            ft.TextButton("Cancelar", on_click=fechar_dialogo_edicao),
            ft.ElevatedButton("Salvar", on_click=salvar_edicao, bgcolor="#A6A6F6", color="black")
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def abrir_edicao(e, ex_id, valor_atual):
        exercicio_em_edicao_id[0] = ex_id
        # Tenta pré-preencher os campos
        try:
            if 'x' in valor_atual:
                s, r = valor_atual.split('x')
                txt_series.value = s
                txt_reps.value = r
            else:
                txt_series.value = valor_atual
                txt_reps.value = ""
        except:
            txt_series.value = ""
            txt_reps.value = ""

        page.open(dialog_edicao)

    # --- Função Principal de Carregamento ---
    def carregar_conteudo():
        container_exercicios.controls.clear()

        # Busca do banco
        exercicios_db = ExercicioController.buscar_por_serie(serie_id)

        # Adiciona Header (Full Width)
        container_exercicios.controls.append(
            ft.Container(
                # Adiciona padding para o texto não colar na borda da tela
                padding=ft.padding.symmetric(horizontal=10),
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    serie_nome,
                                    size=28,
                                    weight=ft.FontWeight.BOLD,
                                    color='#A6A6F6',
                                    expand=True,  # Ocupa espaço disponível
                                    max_lines=2,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.CHECK_CIRCLE_OUTLINE,
                                    icon_color=ft.Colors.GREEN,
                                    icon_size=30,
                                    tooltip='Concluir Treino',
                                    on_click=lambda e: print("Treino concluído!")
                                ),
                            ],
                        ),
                        # Linha divisória agora ocupa toda a largura (sem width fixo)
                        ft.Container(height=1, bgcolor='#A6A6F6'),
                    ]
                )
            )
        )

        if not exercicios_db:
            container_exercicios.controls.append(
                ft.Container(padding=20,
                             content=ft.Text("Nenhum exercício nesta série ainda.", color=ft.Colors.GREY_500))
            )
        else:
            for ex in exercicios_db:
                try:
                    s, r = ex.series_repeticoes.split('x')
                except:
                    s, r = ex.series_repeticoes, "-"

                # Navegação para detalhes
                def ir_detalhes(e, nome=ex.nome):
                    page.session.set("exercicio_atual", nome)
                    page.go('/detalhes_exercicio')

                container_exercicios.controls.append(
                    card_exercicio(
                        nome=ex.nome,
                        series=s,
                        repeticoes=r,
                        grupo_muscular=ex.grupo_muscular,  # Ícone correto
                        on_click=ir_detalhes,
                        on_edit=lambda e, eid=ex.id, val=ex.series_repeticoes: abrir_edicao(e, eid, val)
                    )
                )

        # Botão Inserir no final
        container_exercicios.controls.append(
            ft.Container(
                padding=ft.Padding(top=20, bottom=20, left=0, right=0),
                content=btn_inserir_exercicio(
                    on_click=lambda e: page.go('/selecionar_exercicios')
                )
            )
        )
        page.update()

    # Inicializa
    carregar_conteudo()

    return layout_com_header_fixado(
        page,
        'Série',
        [container_exercicios],  # Passa a coluna dinâmica como conteúdo
        bottom=nav_bar(page, selected_index=2),
    )