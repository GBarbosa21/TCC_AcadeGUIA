from src.database.config import SessionLocal
from src.database.models import Exercicio

class ExercicioController:
    @staticmethod
    def buscar_por_serie(serie_id: int):
        """Retorna todos os exercícios vinculados a uma série específica."""
        db = SessionLocal()
        try:
            # Filtra apenas exercícios que pertencem ao ID da série fornecida
            return db.query(Exercicio).filter(Exercicio.serie_id == serie_id).all()
        finally:
            db.close()

    @staticmethod
    def criar(nome: str, serie_id: int, series_reps: str = "4x12"):
        """Adiciona um novo exercício a uma série."""
        db = SessionLocal()
        try:
            novo_exercicio = Exercicio(
                nome=nome,
                serie_id=serie_id,
                series_repeticoes=series_reps,
                concluido=False
            )
            db.add(novo_exercicio)
            db.commit()
            return novo_exercicio
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

    @staticmethod
    def deletar(exercicio_id: int):
        """Remove um exercício pelo ID."""
        db = SessionLocal()
        try:
            ex = db.query(Exercicio).filter(Exercicio.id == exercicio_id).first()
            if ex:
                db.delete(ex)
                db.commit()
        finally:
            db.close()