from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .config import Base, engine


# --- Tabela de Séries (Minhas Séries) ---
class Serie(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)

    # Relacionamento com os exercícios desta série
    exercicios = relationship("Exercicio", back_populates="serie", cascade="all, delete-orphan")


# --- Tabela de Exercícios (Dentro de uma Série) ---
class Exercicio(Base):
    __tablename__ = "exercicios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    grupo_muscular = Column(String)
    series_repeticoes = Column(String)  # Ex: "4x12"
    concluido = Column(Boolean, default=False)
    serie_id = Column(Integer, ForeignKey("series.id"))
    serie = relationship("Serie", back_populates="exercicios")


# --- Tabela do Catálogo Geral (Lista de Exercícios do App) ---
class CatalogoExercicio(Base):
    __tablename__ = "catalogo_exercicios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    grupo_muscular = Column(String, nullable=False)  # Ex: "Peito", "Costas"

    # Detalhes ricos para a tela de Instruções
    tipo = Column(String)
    musculo_alvo = Column(String)
    dica_preparacao = Column(String)
    dica_excentrica = Column(String)
    dica_concentrica = Column(String)

    # Campo para marcar como Favorito/Salvo
    favorito = Column(Boolean, default=False)


# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)