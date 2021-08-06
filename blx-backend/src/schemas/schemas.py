from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    id:Optional[str]= None
    nome:str
    telefone:str
    #minhasLista: List[Pedido]
    #meusPediso: List[Pedido]

class Produto(BaseModel):
    id:Optional[str]= None
    nome:str
    detalhes:str
    preco:float
    disponivel:bool=False

    """
    Para que os schemas possam ser gerados apartir de modelos 
    """
    class Config:
        orm_mode =True


class Pedido(BaseModel):
    id:Optional[str]= None
    quantidade:int
    entrega: bool= True
    endereço:str
    observacoes:Optional[str]=None
