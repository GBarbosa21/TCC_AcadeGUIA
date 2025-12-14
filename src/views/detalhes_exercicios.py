import flet as ft
from funcoes import layout_com_header_fixado, nav_bar


def detalhes_exercicio(page: ft.Page):
    # Recupera o nome do exercício salvo na sessão (ou usa um padrão se falhar)
    nome_exercicio = page.session.get("exercicio_atual") or "Exercício"

    # --- Conteúdo da Tela ---
    conteudo = [
        # 1. Área Visual (Imagem/Vídeo)
        ft.Container(
            height=250,
            bgcolor=ft.colors.BLACK,
            border_radius=12,
            alignment=ft.alignment.center,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,  # Garante que a imagem respeite a borda arredondada
            content=ft.Stack(
                alignment=ft.alignment.center,
                controls=[
                    # Imagem de Fundo (Placeholder dinâmico com o nome do exercício)
                    ft.Image(
                        src=f"https://placehold.co/600x400/1a1a1a/A6A6F6/png?text={nome_exercicio}",
                        fit=ft.ImageFit.COVER,
                        opacity=0.6,  # Um pouco escuro para destacar o ícone de Play
                        width=1000,  # Garante que cubra a largura
                    ),
                    # Ícone de Play Gigante (simulando player de vídeo)
                    ft.Icon(
                        name=ft.Icons.PLAY_CIRCLE_FILL,
                        size=80,
                        color="#A6A6F6",
                    ),
                ],
            ),
        ),

        # 2. Título "Instruções"
        ft.Text(
            "Instruções de Execução",
            size=22,
            weight=ft.FontWeight.BOLD,
            color="#A6A6F6"
        ),

        # 3. Bloco de Texto com os Passos
        ft.Container(
            padding=20,
            bgcolor=ft.colors.GREY_900,
            border_radius=12,
            content=ft.Column(
                spacing=15,
                controls=[
                    ft.Text("1. Posicione-se corretamente no equipamento ou banco.", size=16, color="#F1F1F1"),
                    ft.Text("2. Mantenha a postura firme e o abdômen contraído.", size=16, color="#F1F1F1"),
                    ft.Text("3. Execute o movimento de forma controlada (concêntrica e excêntrica).", size=16,
                            color="#F1F1F1"),
                    ft.Text("4. Respire: solte o ar na força e puxe o ar na volta.", size=16, color="#F1F1F1"),
                ]
            )
        ),

        # 4. Tags de Músculos (Opcional, mas fica bonito)
        ft.Text("Músculos Trabalhados", size=18, weight=ft.FontWeight.BOLD, color="#A6A6F6"),

        ft.Row(
            spacing=10,
            controls=[
                ft.Container(
                    padding=ft.Padding(15, 8, 15, 8),
                    bgcolor=ft.colors.WHITE10,
                    border_radius=20,
                    content=ft.Text("Primário", color="white")
                ),
                ft.Container(
                    padding=ft.Padding(15, 8, 15, 8),
                    bgcolor=ft.colors.WHITE10,
                    border_radius=20,
                    content=ft.Text("Secundário", color="white")
                ),
            ]
        )
    ]

    return layout_com_header_fixado(
        page,
        nome_exercicio,  # O título da página será o nome do exercício
        conteudo,
        # Mantemos o índice 0 (Exercícios) selecionado
        bottom=nav_bar(page, selected_index=0)
    )