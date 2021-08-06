from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
Pasta de configurações de nosso banco de dados blx
"""


SQLALCHEMY_DATABASE_URL = "sqlite:///./myFlix.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Criando base de dados 
def criar_bd():
    Base.metadata.create_all(bind=engine)

#Obtendo conexões - Sessoes com banco de dados 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    