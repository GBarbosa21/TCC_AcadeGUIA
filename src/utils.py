# utils.py
import flet as ft

# Importa as suas funções de view originais
from src.views.inicio import inicio
from src.views.Minhas_series import minhas_series
from src.views.serie import serie


# A view de exercícios pode ser adicionada aqui quando for criada
# from exercicios import exercicios


def route_change(page: ft.Page):
    """
    Gerencia a navegação, mostrando a view correta para cada rota.
    """

    # Mapeamento das suas rotas para as funções que criam as views
    rotas = {
        '/': inicio,
        '/inicio': inicio,
        '/minhas_series': minhas_series,
        '/serie': serie,
        # "/exercicios": exercicios, # <-- Descomente quando criar a página de exercícios
    }

    # Limpa a tela
    page.views.clear()

    # Encontra a função da view correta. Se a rota não existir, vai para a página inicial.
    view_function = rotas.get(page.route, inicio)

    # Chama a função encontrada (ex: inicio(page)) para obter a View e a exibe
    page.views.append(view_function(page))

    page.update()
