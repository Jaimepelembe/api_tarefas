from pydantic import BaseModel # Serve para definir o formato dos dados

#Ajudar na tipagem
from typing import List, Optional

class Tarefa(BaseModel):
    
    def __init__(self):
        id: Optional[int]=None
        titulo:str
        descricao:str
        concluida:bool=False