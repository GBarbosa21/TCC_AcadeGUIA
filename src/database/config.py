import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Calcula o caminho absoluto da RAIZ do projeto
# __file__ = .../src/database/config.py
# dirname 1 = .../src/database
# dirname 2 = .../src
# dirname 3 = .../ (Raiz do Projeto)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 2. Define o caminho da pasta 'data' e do arquivo '.db'
DATA_DIR = os.path.join(BASE_DIR, 'data')
DB_PATH = os.path.join(DATA_DIR, 'acadeguia.db')

# 3. Cria a pasta 'data' se ela não existir (NO LOCAL CERTO)
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 4. Configura a URL de conexão
DATABASE_URL = f"sqlite:///{DB_PATH}"

# Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()