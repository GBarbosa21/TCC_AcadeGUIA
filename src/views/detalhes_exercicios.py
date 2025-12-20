import flet as ft
from funcoes import layout_com_header_fixado, nav_bar
from controllers.catalogo_controller import CatalogoController


def detalhes_exercicio(page: ft.Page):
    # 1. Recupera o nome do exercício salvo na sessão
    nome_exercicio = page.session.get("exercicio_atual") or "Exercício"

    # 2. Busca os dados reais no Banco de Dados
    exercicio_db = CatalogoController.buscar_por_nome(nome_exercicio)

    # 3. Define as variáveis com base nas colunas exatas da tabela
    if exercicio_db:
        tipo = exercicio_db.tipo or "Geral"
        alvo = exercicio_db.musculo_alvo or "Geral"

        # Mapeamento direto das 3 colunas do banco
        dica1 = exercicio_db.dica_preparacao or "Posicione-se corretamente."
        dica2 = exercicio_db.dica_excentrica or "Controle a descida."
        dica3 = exercicio_db.dica_concentrica or "Faça força mantendo a postura."
    else:
        # Fallback padrão (apenas 3 dicas)
        tipo = "Personalizado"
        alvo = "Geral"
        dica1 = "Posicione-se corretamente no equipamento ou banco."
        dica2 = "Mantenha a postura firme e o abdômen contraído."
        dica3 = "Execute o movimento de forma controlada."

    # --- Conteúdo da Tela ---
    conteudo = [
        # 1. Área Visual (Imagem/Vídeo)
        ft.Container(
            height=250,
            bgcolor=ft.colors.BLACK,
            border_radius=12,
            alignment=ft.alignment.center,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Stack(
                alignment=ft.alignment.center,
                controls=[
                    # Imagem dinâmica
                    ft.Image(
                        src=f"https://placehold.co/600x400/1a1a1a/A6A6F6/png?text={nome_exercicio.replace(' ', '+')}",
                        fit=ft.ImageFit.COVER,
                        opacity=0.6,
                        width=1000,
                    ),
                    # Ícone de Play
                    ft.Icon(
                        name=ft.Icons.PLAY_CIRCLE_FILL,
                        size=80,
                        color="#A6A6F6",
                    ),
                ],
            ),
        ),

        # 2. Cabeçalho com Título e Tipo
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(
                    "Instruções de Execução",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color="#A6A6F6"
                ),
                # Tag com o Tipo
                ft.Container(
                    padding=ft.Padding(10, 5, 10, 5),
                    bgcolor=ft.colors.BLUE_GREY_900,
                    border_radius=8,
                    content=ft.Text(tipo.upper(), size=12, color="white", weight=ft.FontWeight.BOLD)
                )
            ]
        ),

        # 3. Bloco de Texto com as 3 Dicas do Banco
        ft.Container(
            padding=20,
            bgcolor=ft.colors.GREY_900,
            border_radius=12,
            content=ft.Column(
                spacing=15,
                controls=[
                    # Dica 1: Preparação
                    ft.Column(spacing=2, controls=[
                        ft.Text("1. Preparação", weight=ft.FontWeight.BOLD, color="#A6A6F6"),
                        ft.Text(dica1, size=16, color="#F1F1F1"),
                    ]),

                    # Dica 2: Fase Excêntrica
                    ft.Column(spacing=2, controls=[
                        ft.Text("2. Fase Excêntrica (Volta)", weight=ft.FontWeight.BOLD, color="#A6A6F6"),
                        ft.Text(dica2, size=16, color="#F1F1F1"),
                    ]),

                    # Dica 3: Fase Concêntrica
                    ft.Column(spacing=2, controls=[
                        ft.Text("3. Fase Concêntrica (Força)", weight=ft.FontWeight.BOLD, color="#A6A6F6"),
                        ft.Text(dica3, size=16, color="#F1F1F1"),
                    ]),
                ]
            )
        ),

        # 4. Tags de Músculos
        ft.Text("Músculo Alvo", size=18, weight=ft.FontWeight.BOLD, color="#A6A6F6"),

        ft.Row(
            spacing=10,
            controls=[
                ft.Container(
                    padding=ft.Padding(15, 8, 15, 8),
                    bgcolor="#A6A6F6",  # Destaque para o músculo principal
                    border_radius=20,
                    content=ft.Text(alvo, color="black", weight=ft.FontWeight.BOLD)
                ),
            ]
        )
    ]

    return layout_com_header_fixado(
        page,
        nome_exercicio,
        conteudo,
        bottom=nav_bar(page, selected_index=0)
    )