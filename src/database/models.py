from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .config import Base, engine


class Serie(Base):
    __tablename__ = "series"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    exercicios = relationship("Exercicio", back_populates="serie", cascade="all, delete-orphan")


class Exercicio(Base):
    __tablename__ = "exercicios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    series_repeticoes = Column(String)
    concluido = Column(Boolean, default=False)
    serie_id = Column(Integer, ForeignKey("series.id"))
    serie = relationship("Serie", back_populates="exercicios")


class CatalogoExercicio(Base):
    __tablename__ = "catalogo_exercicios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    grupo_muscular = Column(String, nullable=False)
    tipo = Column(String)
    musculo_alvo = Column(String)
    dica_preparacao = Column(String)
    dica_excentrica = Column(String)
    dica_concentrica = Column(String)

    # NOVO CAMPO: Para marcar se está salvo/favoritado
    favorito = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)