# Importar os pacotes 
from pathlib import Path
import sqlite3
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel # Serve para definir o formato dos dados recebidos e enviados nas requisições HTTP

#Ajudar na tipagem
from typing import List, Optional


#Criar a API
app = FastAPI(title="API de Tarefas")



#Modelo de dados
#O Pydantic permite validar automaticamente os dados recebidos nas requisições.
class Tarefa(BaseModel):
        id: Optional[int]=None
        titulo:str
        descricao:str
        concluida:bool=False


#Base de dados
baseDados=Path(__file__).with_name("tarefas.db")

def Conectar():
    conexao=sqlite3.connect(baseDados,timeout=100)
    conexao.row_factory=sqlite3.Row
    return conexao

#Base de dados em memoria
db_tarefas=[ ]


#Criação das rotas: Endpoints

# Rota para a pagina inicial
@app.get("/", response_model=str)
async def paginaInicial():
    return "Bem-vindo a página inicial do gestor de tarefas."

#Rota para listar todas as tarefas
@app.get("/tarefas", response_model=List[Tarefa])
async def listarTarefas():
    """Retorna a lista de todas as tarefas"""
    return db_tarefas


#Rota para buscar a tarefa por ID
@app.get("/tarefas/{id_tarefa}",response_model=Tarefa,status_code=200)
async def buscarTarefaPorID(id_tarefa:int):
    """Retorna uma tarefa pelo seu ID"""
    if id_tarefa>0:
        for tarefa in db_tarefas:
            if tarefa.id == id_tarefa:
                return tarefa
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    else:
        raise HTTPException(status_code=404, detail="Voce digitou um ID incorrecto.")


#Rota para criar uma tarefa
@app.post("/tarefas", response_model=Tarefa,status_code=201)
async def criarTarefa(tarefa:Tarefa):
    """Cria uma nova tarefa"""
    tarefa.id=len(db_tarefas)+1
    db_tarefas.append(tarefa)
    return tarefa

#Rota para actualizar uma tarefa
@app.put("/tarefas/{id_tarefa}",response_model=Tarefa, status_code=200)
async def actualizarTarefa(id_tarefa:int,tarefaActualizada:Tarefa):
    """Actualiza os dados de uma tarefa"""
    if id_tarefa >0:
        for indice,tarefaAntiga in enumerate(db_tarefas):
            if tarefaAntiga.id == id_tarefa:
                tarefaActualizada.id=id_tarefa
                db_tarefas[indice]=tarefaActualizada
                return tarefaActualizada
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    
    else:
        raise HTTPException(status_code=404, detail="Voce digitou um ID incorrecto.")


#Rota para deletar uma tarefa
@app.delete("/tarefas/{id_tarefa}",response_model=str,status_code=200)
async def deletarTarefa(id_tarefa:int):
    """Deleta uma tarefa"""
    if id_tarefa >0:
        for tarefa in db_tarefas:
            if tarefa.id== id_tarefa:
                db_tarefas.remove(tarefa)
                return "Tarefa deletada com sucesso."
                    
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    
    else:
        raise HTTPException(status_code=404, detail="Voce digitou um ID incorrecto.")
