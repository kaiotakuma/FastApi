from typing_extensions import Annotated
from pydantic import BaseModel
from typing import Optional, List

"""
Especificar como vamos receber e entregar nossos dados 

MyFlix - App para cadastro de séries do Netflix
> Série (titulo, ano, genero, qtd_temporadas)


Funcionalidades
Básicas: Cadastrar, Listar, 
Adicionais: Exibir por Id, Listar por Título, Remover

"""

class Serie(BaseModel):
    id:Optional[int] = None
    titulo = str
    ano = int
    genero = str 
    qtdTemporadas = int 
    """
    class Config
    Para que os schemas possam ser gerados apartir de modelos 
    """
    class Config:
        orm_mode =True

