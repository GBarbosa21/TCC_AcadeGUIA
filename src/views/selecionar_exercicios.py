import flet as ft
from funcoes import layout_com_header_fixado, nav_bar, card_exercicio_selecionavel

def selecionar_exercicios(page: ft.Page):
    """View para selecionar novos exercícios para a série."""

    conteudo = [
        # Lista de exercícios com checkbox
        card_exercicio_selecionavel(
            'Supino Reto',
            on_change_check=lambda e: print(f"Supino Reto selecionado: {e.control.value}")
        ),
        card_exercicio_selecionavel(
            'Supino Inclinado',
            on_change_check=lambda e: print(f"Supino Inclinado selecionado: {e.control.value}")
        ),
        card_exercicio_selecionavel(
            'Crucifixo',
            on_change_check=lambda e: print(f"Crucifixo selecionado: {e.control.value}")
        ),
        card_exercicio_selecionavel(
            'Crossover',
            on_change_check=lambda e: print(f"Crossover selecionado: {e.control.value}")
        ),

        # Botão para Confirmar a Inserção
        ft.Container(
            padding=ft.Padding(top=20, bottom=20, left=0, right=0),
            content=ft.ElevatedButton(
                "Adicionar Selecionados",
                height=50,
                width=350,
                style=ft.ButtonStyle(
                    bgcolor="#A6A6F6",
                    color=ft.colors.BLACK,
                    shape=ft.RoundedRectangleBorder(radius=12),
                ),
                # Ao clicar, volta para a série (simulando a inserção)
                on_click=lambda e: page.go('/serie')
            )
        )
    ]

    return layout_com_header_fixado(
        page,
        'Selecionar Exercícios',
        conteudo,
        # Mantemos o índice 2 (Minhas Séries) pois ainda estamos nesse contexto
        bottom=nav_bar(page, selected_index=2),
    )