import flet as ft

# Tratamento de importação para rodar de 'src' ou raiz
try:
    from funcoes import layout_com_header_fixado, nav_bar
    from controllers.catalogo_controller import CatalogoController
except ImportError:
    from src.funcoes import layout_com_header_fixado, nav_bar
    from src.controllers.catalogo_controller import CatalogoController


def detalhes_exercicio(page: ft.Page):
    # 1. Recupera o nome do exercício salvo na sessão
    nome_exercicio = page.session.get("exercicio_atual") or "Exercício"

    # 2. Busca os detalhes RICOS no Banco de Dados
    exercicio_db = CatalogoController.buscar_por_nome(nome_exercicio)

    # 3. Define valores padrão com base nos dados do banco
    if exercicio_db:
        tipo_exercicio = exercicio_db.tipo or "Geral"
        musculo_alvo = exercicio_db.musculo_alvo or "Geral"
        dica1 = exercicio_db.dica_preparacao or "Posicione-se corretamente no equipamento."
        dica2 = exercicio_db.dica_excentrica or "Execute o movimento de descida controlada."
        dica3 = exercicio_db.dica_concentrica or "Realize a força mantendo a postura."
    else:
        # Fallback
        tipo_exercicio = "Customizado"
        musculo_alvo = "Geral"
        dica1 = "Prepare-se para o exercício."
        dica2 = "Execute o movimento com atenção."
        dica3 = "Respire durante a execução."

    # --- Conteúdo da Tela ---
    conteudo = [
        # 1. Área Visual (Imagem/Vídeo)
        ft.Container(
            height=250,
            bgcolor=ft.Colors.BLACK,  # Usando ft.Colors correto
            border_radius=12,
            alignment=ft.alignment.center,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Stack(
                alignment=ft.alignment.center,
                controls=[
                    ft.Image(
                        src=f"https://placehold.co/600x400/1a1a1a/A6A6F6/png?text={nome_exercicio.replace(' ', '+')}",
                        fit=ft.ImageFit.COVER,
                        opacity=0.6,
                        width=1000,
                    ),
                    ft.Icon(
                        name=ft.Icons.PLAY_CIRCLE_FILL,
                        size=80,
                        color="#A6A6F6",
                    ),
                ],
            ),
        ),

        # 2. Cabeçalho de Instruções + Tag de Tipo
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(
                    "Instruções",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color="#A6A6F6"
                ),
                ft.Container(
                    padding=ft.Padding(10, 5, 10, 5),
                    bgcolor=ft.Colors.BLUE_GREY_900,
                    border_radius=8,
                    content=ft.Text(str(tipo_exercicio).upper(), size=12, color="white", weight=ft.FontWeight.BOLD)
                )
            ]
        ),

        # 3. Bloco de Texto com os Passos
        ft.Container(
            padding=20,
            bgcolor=ft.Colors.GREY_900,
            border_radius=12,
            content=ft.Column(
                spacing=15,
                controls=[
                    ft.Column(spacing=2, controls=[
                        ft.Text("1. Preparação", weight=ft.FontWeight.BOLD, color="#A6A6F6"),
                        ft.Text(dica1, size=16, color="#F1F1F1"),
                    ]),
                    ft.Column(spacing=2, controls=[
                        ft.Text("2. Fase Excêntrica (Volta)", weight=ft.FontWeight.BOLD, color="#A6A6F6"),
                        ft.Text(dica2, size=16, color="#F1F1F1"),
                    ]),
                    ft.Column(spacing=2, controls=[
                        ft.Text("3. Fase Concêntrica (Força)", weight=ft.FontWeight.BOLD, color="#A6A6F6"),
                        ft.Text(dica3, size=16, color="#F1F1F1"),
                    ]),
                ]
            )
        ),

        # 4. Músculo Alvo
        ft.Text("Foco Muscular", size=18, weight=ft.FontWeight.BOLD, color="#A6A6F6"),

        ft.Row(
            controls=[
                ft.Container(
                    padding=ft.Padding(15, 8, 15, 8),
                    bgcolor="#A6A6F6",
                    border_radius=20,
                    content=ft.Text(musculo_alvo, color="black", weight=ft.FontWeight.BOLD)
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