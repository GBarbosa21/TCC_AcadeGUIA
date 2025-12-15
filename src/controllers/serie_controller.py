from src.database.config import SessionLocal
from src.database.models import Serie

class SerieController:
    @staticmethod
    def buscar_todas():
        """Busca todas as séries e conta quantos exercícios cada uma tem."""
        db = SessionLocal()
        try:
            series = db.query(Serie).all()
            # Convertemos para uma lista de dicionários para facilitar o uso na View
            dados = []
            for s in series:
                dados.append({
                    "id": s.id,
                    "nome": s.nome,
                    "qtd_exercicios": len(s.exercicios) # Conta real do banco
                })
            return dados
        finally:
            db.close()

    @staticmethod
    def criar(nome: str):
        """Cria uma nova série no banco de dados."""
        db = SessionLocal()
        try:
            nova_serie = Serie(nome=nome)
            db.add(nova_serie)
            db.commit()
            return nova_serie
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

    @staticmethod
    def deletar(id_serie: int):
        """Remove uma série pelo ID."""
        db = SessionLocal()
        try:
            serie = db.query(Serie).filter(Serie.id == id_serie).first()
            if serie:
                db.delete(serie)
                db.commit()
        finally:
            db.close()