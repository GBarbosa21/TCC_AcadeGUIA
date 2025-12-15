from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .config import Base, engine


# Observação: Removemos o modelo 'Usuario' e a importação do 'bcrypt'.
# O aplicativo agora funciona como um armazenamento local (single-user por dispositivo),
# focando na privacidade total dos dados (nada sai do dispositivo).

class Serie(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)


    exercicios = relationship("Exercicio", back_populates="serie", cascade="all, delete-orphan")


class Exercicio(Base):
    __tablename__ = "exercicios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    series_repeticoes = Column(String)  # Ex: "4x12"
    concluido = Column(Boolean, default=False)

    serie_id = Column(Integer, ForeignKey("series.id"))
    serie = relationship("Serie", back_populates="exercicios")


# Esta tabela guarda a lista "padrão" para seleção
class CatalogoExercicio(Base):
    __tablename__ = "catalogo_exercicios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    grupo_muscular = Column(String, nullable=False)  # Ex: "Peito", "Costas"

    # Novos campos para enriquecer o app
    tipo = Column(String)  # Composto ou Isolado
    musculo_alvo = Column(String)  # Ex: Peitoral Maior
    dica_preparacao = Column(String)  # Dica 1
    dica_excentrica = Column(String)  # Dica 2
    dica_concentrica = Column(String)  # Dica 3


# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)