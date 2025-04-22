import flet as ft
import Styles


def main(page: ft.Page):
    page.title="AcadeGUIA"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.favicon="assets/favicon.png"

    card_Opção(
        
    )

ft.app(view=ft.AppView.FLET_APP, target=main)
