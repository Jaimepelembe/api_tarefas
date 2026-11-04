# Importar os pacotes 
from pathlib import Path
import sqlite3
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel # Serve para definir o formato dos dados recebidos e enviados nas requisições HTTP
#Modelo de dados
from tarefa import Tarefa

#Ajudar na tipagem
from typing import List, Optional

from base_dados.gestorBD import GestorBD


#Criar a API
app = FastAPI(title="API de Tarefas")

#Base de dados em memoria
db_tarefas=[ ]
gestorBD=GestorBD()

#Criação das rotas: Endpoints

# Rota para a pagina inicial
@app.get("/", response_model=str)
async def paginaInicial():
    return "Bem-vindo a página inicial do gestor de tarefas."

#Rota para listar todas as tarefas
@app.get("/tarefas", response_model=List[Tarefa])
async def listarTarefas():
    """Retorna a lista de todas as tarefas"""
    return gestorBD.buscarTodasTarefas()
    #return db_tarefas


#Rota para buscar a tarefa por ID
@app.get("/tarefas/{id_tarefa}",response_model=Tarefa,status_code=200)
async def buscarTarefaPorID(id_tarefa:int):
    """Retorna uma tarefa pelo seu ID"""
    if id_tarefa>0:
        tarefa= gestorBD.buscarTarefaPorID(id_tarefa)
        if tarefa ==None:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
        else:
            return tarefa
    else:
        raise HTTPException(status_code=404, detail="Voce digitou um ID incorrecto.")


#Rota para criar uma tarefa
@app.post("/tarefas", response_model=Tarefa,status_code=201)
async def criarTarefa(tarefa:Tarefa):
    """Cria uma nova tarefa"""
    tarefa=gestorBD.criarTarefa(tarefa)
    return tarefa

#Rota para actualizar uma tarefa
@app.put("/tarefas/{id_tarefa}",response_model=Tarefa, status_code=200)
async def editarTarefa(id_tarefa:int,tarefaActualizada:Tarefa):
    """Actualiza os dados de uma tarefa"""
    if id_tarefa >0:
        tarefa=gestorBD.editarTarefa(id_tarefa,tarefaActualizada)
        if tarefa!=None:
            return tarefa
        else:
            raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    
    else:
        raise HTTPException(status_code=404, detail="Voce digitou um ID incorrecto.")


#Rota para deletar uma tarefa
@app.delete("/tarefas/{id_tarefa}",response_model=str,status_code=200)
async def deletarTarefa(id_tarefa:int):
    """Deleta uma tarefa"""
    if id_tarefa >0:
        mensagem=gestorBD.deletarTarefa(id_tarefa)
        if mensagem!=None:
            return mensagem
        else:               
            raise HTTPException(status_code=404, detail="Tarefa nao foi apagada")
    
    else:
        raise HTTPException(status_code=404, detail="Voce digitou um ID incorrecto.")
