# Importar os pacotes 
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel # Serve para definir o formato dos dados

#Ajudar na tipagem
from typing import List, Optional


#Criar a API
app = FastAPI(title="API de Tarefas")





class Tarefa(BaseModel):
    
    def __init__(self):
        id: Optional[int]=None
        titulo:str
        descricao:str
        concluida:bool=False

#Modelo de dados


#Base de dados em memoria
db_tarefas=[   {
    "titulo": "Estudar Python",
    "descricao": "Revisar funções, listas e dicionários.",
    "concluida": False
    }]


#Criação das rotas

# Rota para a pagina inicial
@app.get("/", response_model=str)
async def paginaInicial():
    return "Bem-vindo a página inicial do gestor de tarefas."

#Rota para listar todas as tarefas
@app.get("/tarefas", response_model=List[Tarefa])
async def listarTarefas():
    return db_tarefas


#Rota para criar uma tarefa
@app.get("/tarefas", response_model=Tarefa)
async def listarTarefas():
    return db_tarefas



