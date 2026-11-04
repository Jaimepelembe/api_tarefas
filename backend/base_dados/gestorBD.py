from pathlib import Path
import sqlite3
from tarefa import Tarefa


#Base de dados
baseDados=Path(__file__).with_name("tarefas.db")
print(baseDados)

class GestorBD:
    
    def __init__(self):
        self.criarTabela()
        self.inserirDadosExemplo()
        
    def conectar(self):
        try:
            conexao=sqlite3.connect(baseDados,timeout=10) #timeout de 10 segundos
            conexao.row_factory=sqlite3.Row
            return conexao
        except sqlite3.OperationalError as e:
            print(f"Erro operacional no SQLite: {e}")
        except sqlite3.DatabaseError as e:
            print(f"Erro na base de dados: {e}")
        except Exception as e:
            print("Erro ao conectar a base de dados: {e}")
        
    def criarTabela(self):
        """Cria a tabela de tarefa, caso ela não exista"""
        conexao= self.conectar()
        
        try:
            cursor=conexao.cursor()
            comandoSql="CREATE TABLE IF NOT EXISTS tarefa (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL CHECK (LENGTH(titulo)<=64), descricao TEXT NOT NULL CHECK(LENGTH(descricao)<=128), concluida INTEGER NOT NULL);"
            cursor.execute(comandoSql)
            conexao.commit()
        
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")
        except sqlite3.Error as e:
            print(f"Erro geral do SQLite: {e}")
        
        finally:
            conexao.close()
        
        
    def inserirDadosExemplo(self):
        """Inseri algumas tarefas como exemplo"""
        conexao= self.conectar()
        
        try:        
            cursor=conexao.cursor()
            comandoSql="SELECT COUNT(*) FROM tarefa"
            cursor.execute(comandoSql)
            quantidadeLinhas=cursor.fetchone()[0]
            
            if quantidadeLinhas ==0:
                comandoSql="INSERT INTO tarefa (titulo,descricao,concluida) VALUES (?,?,?)"
                exemploTarefas=[("Curso de Python","Curso de desenvolvimento desktop em Python",0),("Curso de IA","Curso de analise de analise de dados utilizando IA",1),("Curso de Programacao Web","Curso de programacao Web utilizando HTML5, CSS3, JS e PHP",0)]
                cursor.executemany(comandoSql,exemploTarefas)
                conexao.commit()
        
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")
        except sqlite3.Error as e:
            print(f"Erro geral do SQLite: {e}")
        
        finally:
            conexao.close()   
    
    def criarTarefa(self,tarefa:Tarefa)->Tarefa:
        """Cria uma nova tarefa"""
        conexao= self.conectar()  
        try:  
        
            cursor=conexao.cursor()
            comandoSql="INSERT INTO tarefa(titulo,descricao,concluida) VALUES(?,?,?)"
            dadosTarefa=(tarefa.titulo,tarefa.descricao,tarefa.concluida)
            cursor.execute(comandoSql,dadosTarefa)
            conexao.commit()
            id_tarefa=cursor.lastrowid
            tarefa.id=id_tarefa
            return tarefa
        
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")
        except sqlite3.Error as e:
            print(f"Erro geral do SQLite: {e}")
        
        finally:
            conexao.close()    
    
    
    def editarTarefa(self,id_tarefa,tarefa:Tarefa)->Tarefa:
        """Editar uma tarefa"""
        conexao= self.conectar()  
        try:  
        
            cursor=conexao.cursor()
            comandoSql="UPDATE tarefa SET titulo=?,descricao=?,concluida=? WHERE id=?"
            dadosTarefa=(tarefa.titulo,tarefa.descricao,tarefa.concluida,id_tarefa)
            cursor.execute(comandoSql,dadosTarefa)
            conexao.commit()
            tarefa.id=id_tarefa
            return tarefa
        
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")
        except sqlite3.Error as e:
            print(f"Erro geral do SQLite: {e}")
        
        finally:
            conexao.close()    
        
    def buscarTodasTarefas(self)->list:
        """Retorna todas as tarefas registadas na base de dados"""
        conexao= self.conectar()    
        try:  
        
            comandoSql="SELECT * FROM tarefa"
            cursor=conexao.cursor()
            cursor.execute(comandoSql)        
            return [dict(tarefa) for tarefa in cursor.fetchall()]
    
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")
        except sqlite3.Error as e:
            print(f"Erro geral do SQLite: {e}")
        
        finally:
            conexao.close()            
        
    def buscarTarefaPorID(self,id_tarefa:int):
        """Retorna uma tarefa pelo seu ID"""
        conexao= self.conectar()    
        try:  
            comandoSql="SELECT * FROM tarefa WHERE id=?"
            cursor=conexao.cursor()
            cursor.execute(comandoSql,(id_tarefa,))
            tarefa=cursor.fetchone()
            return dict(tarefa) if tarefa else None

        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")
        except sqlite3.Error as e:
            print(f"Erro geral do SQLite: {e}")
        
        finally:
            conexao.close()      
     
    def deletarTarefa(self,id_tarefa)->str:
        """Deleta uma tarefa"""
        conexao= self.conectar()  
        try:  
        
            cursor=conexao.cursor()
            comandoSql="DELETE FROM tarefa WHERE id=?"
            dadosTarefa=(id_tarefa,)
            cursor.execute(comandoSql,dadosTarefa)
            conexao.commit()
            
            if cursor.rowcount>0:
                return "Tarefa deletada com sucesso."
            else:
                return None
        
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
        except sqlite3.OperationalError as e:
            print(f"Erro operacional: {e}")
        except sqlite3.Error as e:
            print(f"Erro geral do SQLite: {e}")
        
        finally:
            conexao.close()  
    
"""
gestor=GestorBD()
tarefas=gestor.buscarTarefaPorID(1)
print(tarefas)

for tarefa in tarefas:
    print(tarefa.get("id"))
    print(tarefa.get("titulo"))
    print(tarefa.get("descricao"))
    print(tarefa.get("concluida"))
    print("---------------")
    """