from src.infra.sqlachemy.config.database import Base

from sqlachemy import Column, Integer, String, Float, Boolean


class Serie(Base):
    #Criando meta atributo no Bd
    __tablename__ = 'serie'
    id = Column(Integer,primary_key=True,index=True)
    titulo = Column(String)
    ano = Column(Integer)
    genero = Column(str)
    qtdTemporadas = Column(Integer)
