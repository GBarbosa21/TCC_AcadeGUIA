import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cria a pasta 'data' se não existir, para organizar o arquivo .db
if not os.path.exists('data'):
    os.makedirs('data')

# Caminho do banco de dados (SQLite para local, mas fácil de mudar para Nuvem)
DATABASE_URL = "sqlite:///data/acadeguia.db"

# Engine segura do SQLAlchemy
# check_same_thread=False é necessário apenas para SQLite + GUI Apps
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False # Mude para True se quiser ver os SQLs no terminal (Debug)
)

# Sessão de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os Models
Base = declarative_base()

def get_db():
    """
    Função geradora para dependência de banco de dados.
    Garante que a conexão abra e FECHE com segurança após o uso.
    Evita vazamento de memória e conexões presas.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()