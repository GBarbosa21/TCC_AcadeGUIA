try:
    from database.config import SessionLocal
    from database.models import CatalogoExercicio
except ImportError:
    from src.database.config import SessionLocal
    from src.database.models import CatalogoExercicio


class ExerciciosSalvosController:
    @staticmethod
    def buscar_apenas_salvos(grupo=None, termo=None):
        """
        Retorna apenas os exercícios marcados como FAVORITOS.
        Suporta filtros de grupo e texto.
        """
        db = SessionLocal()
        try:
            # Filtro base: Apenas os favoritos
            query = db.query(CatalogoExercicio).filter(CatalogoExercicio.favorito == True)

            # Filtros adicionais (igual ao catálogo, mas restrito aos favoritos)
            if grupo:
                query = query.filter(CatalogoExercicio.grupo_muscular == grupo)

            if termo:
                query = query.filter(CatalogoExercicio.nome.ilike(f"%{termo}%"))

            return query.all()
        finally:
            db.close()

    @staticmethod
    def alternar_status_favorito(nome_exercicio: str):
        """
        Salva ou Remove um exercício dos favoritos (Toggle).
        Retorna o novo estado (True = Salvo, False = Removido).
        """
        db = SessionLocal()
        try:
            exercicio = db.query(CatalogoExercicio).filter(CatalogoExercicio.nome == nome_exercicio).first()
            if exercicio:
                # Inverte o valor atual (Se era True vira False, e vice-versa)
                exercicio.favorito = not exercicio.favorito
                db.commit()
                return exercicio.favorito
            return False
        except Exception as e:
            db.rollback()
            print(f"Erro ao salvar favorito: {e}")
            return False
        finally:
            db.close()