from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List,Optional
from pydantic import BaseModel
from uuid import uuid4

app=FastAPI()


origins = ['http://127.0.0.1:5500'] #Ajustando Cor para onde minha aplicação web está hospedada.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel):
    id:Optional[str] #Optinal deixa a atribuição ser opcional
    nome:str
    idade:int
    sexo:str
    cor:str

banco:List[Animal] = []

@app.post('/animais')
def criaAnimal(animal:Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    
    return None

@app.get('/animais')
def listarAnimais():
    print(banco)
    return banco

@app.delete('/animais/{id}')
def excluirDado(id:str):
    for animal in banco:
        if(animal.id ==id ):
            banco.remove(animal)
    return "Operação concluida"
@app.delete('/animais')
def limpandoBanco():
    banco.clear()
    return "Banco resetado"

@app.get('/animais/{id}')
def recebeAnimal(id:str):
    for animal in banco:
        if(animal.id ==id ):
            return {"Animal":animal}
    return {"saida":f"Id {id} não consta no banco de dados "}


    
