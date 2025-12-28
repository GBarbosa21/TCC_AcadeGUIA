# utils.py
import flet as ft

# Importa as suas funções de view originais
try:
    # Forma 1: Executando de dentro de src (sem prefixo)
    from views.inicio import inicio
    from views.Minhas_series import minhas_series
    from views.serie import serie
    from views.exercicios import exercicio_info
    from views.selecionar_exercicios import selecionar_exercicios
    from views.exercicios_salvos import exercicios_salvos_info
    from views.detalhes_exercicios import detalhes_exercicio
except ImportError:
    # Forma 2: Executando da raiz do projeto (com prefixo src.)
    from src.views.inicio import inicio
    from src.views.Minhas_series import minhas_series
    from src.views.serie import serie
    from src.views.exercicios import exercicio_info
    from src.views.selecionar_exercicios import selecionar_exercicios
    from src.views.exercicios_salvos import exercicios_salvos_info
    from src.views.detalhes_exercicios import detalhes_exercicio


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
        "/exercicios": exercicio_info,
        '/exercicios_salvos': exercicios_salvos_info,
        '/selecionar_exercicios': selecionar_exercicios,
        '/detalhes_exercicio': detalhes_exercicio
    }

    # Limpa a tela
    page.views.clear()

    # Encontra a função da view correta. Se a rota não existir, vai para a página inicial.
    view_function = rotas.get(page.route, inicio)

    # Chama a função encontrada (ex: inicio(page)) para obter a View e a exibe
    page.views.append(view_function(page))

    page.update()
