# Minhas_series.py
import flet as ft
from ..funcoes import layout_com_header_fixado, nav_bar, btn_nova_serie, criar_card_serie


def minhas_series(page: ft.Page):
    print("--- DEBUG: Carregando a view 'minhas_series' ---")

    # --- 1. LÓGICA DO POP-UP ---
    txt_nome_serie = ft.TextField(label="Nome da Série", autofocus=True)

    def close_dialog(e):
        print("--- DEBUG: close_dialog chamada ---")
        page.dialog.open = False
        page.update()

    def criar_serie_e_fechar(e):
        print("--- DEBUG: criar_serie_e_fechar chamada ---")
        nome_da_serie = txt_nome_serie.value

        if nome_da_serie:
            novo_card = criar_card_serie(
                nome=nome_da_serie,
                qtd_exercicios=0,
                on_click=lambda e: e.page.go('/serie'),
                on_delete=lambda: print(f"Excluir série {nome_da_serie}")
            )
            lista_de_cards.controls.append(novo_card)

            txt_nome_serie.value = ""
            page.dialog.open = False
            print("--- DEBUG: Nova série criada. Fechando pop-up. ---")
            page.update()
        else:
            txt_nome_serie.error_text = "O nome não pode ser vazio"
            txt_nome_serie.update()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Criar Nova Série"),
        content=txt_nome_serie,
        actions=[
            ft.TextButton("Cancelar", on_click=close_dialog),
            ft.TextButton("Criar", on_click=criar_serie_e_fechar),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Função "Gatilho" para ABRIR o pop-up
    def open_dialog(e):
        print("--- DEBUG: open_dialog FOI CHAMADA ---")  # <-- MENSAGEM MAIS IMPORTANTE
        page.dialog = dialog
        page.dialog.open = True
        page.update()
        print("--- DEBUG: page.update() foi chamado após abrir diálogo ---")

    # --- 2. CONTEÚDO VISUAL DA PÁGINA ---

    lista_de_cards = ft.Column(
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            criar_card_serie(
                'Peito', 4,
                on_click=lambda e: e.page.go('/serie'),
                on_delete=lambda: print('Excluir série Peito'),
            ),
            criar_card_serie(
                'Costas', 5,
                on_click=lambda e: e.page.go('/serie'),
                on_delete=lambda: print('Excluir série Costas'),
            ),
        ]
    )

    print("--- DEBUG: Criando botão 'Nova Série' ---")

    conteudo_da_pagina = [
        btn_nova_serie(
            on_click=open_dialog  # <-- Conecta o botão para abrir o pop-up
        ),
        lista_de_cards
    ]

    print("--- DEBUG: Retornando a View para o layout ---")

    # --- 3. RETORNO DA VIEW ---
    return layout_com_header_fixado(
        page,
        'Minhas Séries',
        conteudo_da_pagina,
        bottom=nav_bar(page, selected_index=2),
    )