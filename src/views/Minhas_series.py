import flet as ft
from funcoes import layout_com_header_fixado, nav_bar, btn_nova_serie, criar_card_serie
from controllers.serie_controller import SerieController


def minhas_series(page: ft.Page):
    # --- Container para os Cards (Dinâmico) ---
    lista_de_cards = ft.Column(
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # --- Função de Navegação Inteligente ---
    def abrir_serie(serie_id, serie_nome):
        # Salva na memória temporária qual série estamos a ver
        # Isso conecta com a lógica que acabamos de fazer em serie.py
        page.session.set("serie_atual_id", serie_id)
        page.session.set("serie_atual_nome", serie_nome)
        page.go('/serie')

    # --- Função para Carregar/Recarregar Dados do Banco ---
    def carregar_series():
        lista_de_cards.controls.clear()
        dados = SerieController.buscar_todas()

        for serie in dados:
            # Cria o card conectando o clique à função abrir_serie
            card = criar_card_serie(
                nome=serie["nome"],
                qtd_exercicios=serie["qtd_exercicios"],
                # Passa o ID e Nome específicos desta série
                on_click=lambda e, sid=serie["id"], snome=serie["nome"]: abrir_serie(sid, snome),
                on_delete=lambda sid=serie["id"]: deletar_serie_action(sid)
            )
            lista_de_cards.controls.append(card)

        page.update()

    def deletar_serie_action(id_serie):
        SerieController.deletar(id_serie)
        carregar_series()  # Atualiza a tela após deletar
        print(f"Série {id_serie} deletada do banco.")

    # --- Lógica do Pop-up ---
    txt_nome_serie = ft.TextField(label="Nome da Série", autofocus=True)

    def close_dialog(e):
        page.close(dialog)

    def criar_serie_e_fechar(e):
        nome_da_serie = txt_nome_serie.value

        if nome_da_serie:
            # 1. Salva no Banco Seguro
            SerieController.criar(nome_da_serie)

            # 2. Atualiza a Interface
            carregar_series()

            # 3. Limpa e fecha
            txt_nome_serie.value = ""
            page.close(dialog)
        else:
            txt_nome_serie.error_text = "O nome não pode ser vazio"
            txt_nome_serie.update()

    # Criamos o diálogo
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

    def open_dialog(e):
        # Usa page.open para garantir que abra sobre qualquer view
        page.open(dialog)

    # --- Carregamento Inicial ---
    # Carrega as séries do banco assim que a tela é montada
    carregar_series()

    conteudo_da_pagina = [
        btn_nova_serie(on_click=open_dialog),
        lista_de_cards
    ]

    return layout_com_header_fixado(
        page,
        'Minhas Séries',
        conteudo_da_pagina,
        bottom=nav_bar(page, selected_index=2),
    )