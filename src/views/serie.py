from src.funcoes import *

def serie():
    return layout_com_header_fixado(
        "Minhas Séries",
        [
            ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    spacing=20,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        btn_nova_serie(on_click=lambda e: e.page.go("/nova_serie"))
                    ]
                )
            ),
            criar_card_serie(
                "Peito",
                4,
                on_click=lambda e: e.page.go("/serie"),
                on_delete=lambda: print("Excluir série Peito")
            ),
        ],
        nav_bar
    )