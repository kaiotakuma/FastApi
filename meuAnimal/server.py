from fastapi import FastAPI
from typing import List,Optional
from pydantic import BaseModel
from uuid import uuid4

app=FastAPI()

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

@app.get('/animais/{id}')
def recebeAnimal(id:str):
    for animal in banco:
        if(animal.id ==id ):
            return {"Animal":animal}
    return {"saida":f"Id {id} não consta no banco de dados "}


    
