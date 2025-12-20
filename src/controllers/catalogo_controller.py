# Ajuste de importação para rodar a partir da pasta src ou raiz
try:
    from database.config import SessionLocal
    from database.models import CatalogoExercicio
except ImportError:
    # Fallback caso esteja rodando de fora da pasta src
    from src.database.config import SessionLocal
    from src.database.models import CatalogoExercicio


class CatalogoController:
    @staticmethod
    def buscar_todos():
        """Retorna todos os exercícios do catálogo."""
        db = SessionLocal()
        try:
            return db.query(CatalogoExercicio).all()
        finally:
            db.close()

    @staticmethod
    def buscar_filtrado(grupo=None, termo=None):
        """Busca com filtros combinados (Grupo e/ou Texto)."""
        db = SessionLocal()
        try:
            query = db.query(CatalogoExercicio)

            # Aplica filtro de grupo muscular se houver
            if grupo:
                query = query.filter(CatalogoExercicio.grupo_muscular == grupo)

            # Aplica filtro de texto (busca por nome) se houver
            if termo:
                # ilike faz a busca ser insensível a maiúsculas/minúsculas
                query = query.filter(CatalogoExercicio.nome.ilike(f"%{termo}%"))

            return query.all()
        finally:
            db.close()

    @staticmethod
    def buscar_por_nome(nome: str):
        """
        Busca os detalhes completos de um exercício pelo nome exato.
        Retorna o objeto com: nome, tipo, musculo_alvo, dica_preparacao, etc.
        """
        db = SessionLocal()
        try:
            return db.query(CatalogoExercicio).filter(CatalogoExercicio.nome == nome).first()
        finally:
            db.close()