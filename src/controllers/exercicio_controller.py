# Ajuste de importação para rodar a partir da pasta src ou raiz
try:
    from database.config import SessionLocal
    from database.models import Exercicio
except ImportError:
    # Fallback caso esteja rodando de fora da pasta src
    from src.database.config import SessionLocal
    from src.database.models import Exercicio

class ExercicioController:
    @staticmethod
    def buscar_por_serie(serie_id: int):
        """Retorna todos os exercícios vinculados a uma série específica."""
        db = SessionLocal()
        try:
            return db.query(Exercicio).filter(Exercicio.serie_id == serie_id).all()
        finally:
            db.close()

    @staticmethod
    def criar(nome: str, serie_id: int, grupo_muscular: str, series_reps: str = "4x12"):
        """Adiciona um novo exercício a uma série."""
        db = SessionLocal()
        try:
            novo_exercicio = Exercicio(
                nome=nome,
                grupo_muscular=grupo_muscular, # Salva o grupo para o ícone correto
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
    def atualizar(exercicio_id: int, series_reps: str):
        """Atualiza as séries e repetições de um exercício."""
        db = SessionLocal()
        try:
            ex = db.query(Exercicio).filter(Exercicio.id == exercicio_id).first()
            if ex:
                ex.series_repeticoes = series_reps
                db.commit()
                return True
            return False
        except Exception as e:
            db.rollback()
            print(f"Erro ao atualizar: {e}")
            return False
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