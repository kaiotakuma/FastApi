from typing import Optional
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

@app.get("/p/{nome}")
def read_root(nome:str):
    texto = f'Olá {nome } tudo bem ? '
    return {texto}

@app.get("/numero/{numero}")
def raiz(numero:int):
    raiz = numero ** 0.5
    texto = f"A raiz do numero {numero} é {raiz}"
    return {"Resultado":texto}

@app.get('/par')
def Par(numero:int):
    if(numero%2 == 0):
        return {"Resultado": f'O numero {numero} é Par'}
    return {"Resultado": f'O numero {numero} é Impar'}

@app.get('/produto')
def p(a:int,b:int):
    def quadrado(a,b):
        a = a**2
        b = b**2
        return a,b
    a,b = quadrado(a,b)
    return {"Resultado":a*b}
class Produto(BaseModel):
    nome: str
    valor: float

@app.post('/venda')
def venda(produto: Produto):
    return {"Mensagem":f"Produto ({produto.nome} - {produto.nome}) R$ cadastrado com sucesso"}