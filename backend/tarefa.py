from pydantic import BaseModel # Serve para definir o formato dos dados

#Ajudar na tipagem
from typing import Optional

#Modelo de dados
#O Pydantic permite validar automaticamente os dados recebidos nas requisições.
class Tarefa(BaseModel):
        id: Optional[int]=None
        titulo:str
        descricao:str
        concluida:bool=False