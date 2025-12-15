import flet as ft
from funcoes import layout_com_header_fixado, nav_bar, card_exercicio, btn_inserir_exercicio
from controllers.exercicio_controller import ExercicioController


def serie(page: ft.Page):
    """View dinâmica que lista exercícios de uma série específica."""

    # 1. Recupera dados da sessão (Segurança/Usabilidade)
    # Estes dados foram salvos quando clicaste no card em "Minhas Séries"
    serie_id = page.session.get("serie_atual_id")
    serie_nome = page.session.get("serie_atual_nome") or "Série"

    # Se por algum motivo não houver ID (ex: refresh direto), mostra erro ou volta
    if not serie_id:
        return ft.View(controls=[ft.Text("Erro: Nenhuma série selecionada. Volte para o início.")])

    # 2. Busca exercícios reais do Banco de Dados
    exercicios_db = ExercicioController.buscar_por_serie(serie_id)

    # 3. Monta a lista visual
    lista_conteudo = [
        # Cabeçalho
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(serie_nome, size=32, weight=ft.FontWeight.BOLD, color='#A6A6F6'),
                ft.IconButton(
                    icon=ft.Icons.CHECK_CIRCLE_OUTLINE,
                    icon_color=ft.Colors.GREEN,
                    icon_size=30,
                    tooltip='Concluir Treino',
                    on_click=lambda e: print("Treino concluído! (Lógica futura)")
                ),
            ],
        ),
        ft.Container(height=1, width=200, bgcolor='#A6A6F6'),
    ]

    # Adiciona os cards dos exercícios vindos do banco
    if not exercicios_db:
        # Mensagem opcional se a lista estiver vazia
        lista_conteudo.append(
            ft.Container(
                padding=20,
                content=ft.Text("Nenhum exercício nesta série ainda.", color=ft.Colors.GREY_500)
            )
        )
    else:
        for ex in exercicios_db:
            # Tenta separar "4x12" em Séries e Repetições para exibir no card
            try:
                s, r = ex.series_repeticoes.split('x')
            except ValueError:
                s, r = "-", "-"

            lista_conteudo.append(
                card_exercicio(
                    nome=ex.nome,
                    series=s,
                    repeticoes=r,
                    # Ao clicar, vai para a lista geral ou detalhes (conforme seu fluxo)
                    on_click=lambda e: page.go('/exercicios')
                )
            )

    # Adiciona o botão de Inserir no final da lista
    lista_conteudo.append(
        ft.Container(
            padding=ft.Padding(top=20, bottom=20, left=0, right=0),
            content=btn_inserir_exercicio(
                # Navega para a tela de seleção para adicionar novos itens
                on_click=lambda e: page.go('/selecionar_exercicios')
            )
        )
    )

    return layout_com_header_fixado(
        page,
        'Série',  # Título da AppBar
        lista_conteudo,
        bottom=nav_bar(page, selected_index=2),
    )