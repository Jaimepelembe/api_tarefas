# Importar os pacotes 
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel # Serve para definir o formato dos dados

#Ajudar na tipagem
from typing import List, Optional

#Criar a API
app = FastAPI(title="API de Tarefas")


#Modelo de dados


#Base de dados em memoria
db_tarefas=[]