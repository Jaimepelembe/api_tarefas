# 🐍 API de Tarefas com FastAPI + SQLite

Projeto de **backend em Python utilizando FastAPI**, desenvolvido com foco no aprendizado prático de **APIs REST, operações CRUD e persistência de dados com SQLite**.

O projeto começou com uma API que armazenava as tarefas em uma lista na memória. Nessa primeira versão, os dados eram perdidos sempre que o servidor era reiniciado.

Agora evoluímos a aplicação para utilizar um **banco de dados SQLite**, permitindo que as tarefas continuem armazenadas mesmo após reiniciar a API.

> **Uma aplicação, várias evoluções. Primeiro aprendemos a construir o CRUD. Agora aprendemos a salvar os dados de verdade!**

Projeto desenvolvido ao vivo no canal **Desvendando o Código**, com explicações passo a passo, implementação prática e testes utilizando o Swagger.

---

## 📺 Acompanhe a evolução do projeto

### Parte 01 — Criando uma API REST com FastAPI

Na primeira aula, desenvolvemos um CRUD completo utilizando uma lista em memória para armazenar as tarefas.

**Conteúdo:**
- Introdução ao FastAPI
- Criação de uma API REST
- Modelo de dados com Pydantic
- Implementação das rotas GET, POST, PUT e DELETE
- Testes com Swagger
- Armazenamento temporário em memória

🎥 **Assista à Parte 01:**

https://youtube.com/live/c4bCbxPQ23c

### Parte 02 — Persistência de Dados com SQLite

Nesta etapa, evoluímos o projeto para utilizar um banco de dados SQLite, substituindo o armazenamento temporário em memória.

**Conteúdo:**
- Introdução à persistência de dados
- Conexão com SQLite utilizando `sqlite3`
- Criação automática do banco e da tabela
- Operações SQL: INSERT, SELECT, UPDATE e DELETE
- Consultas e manipulação de tarefas
- Tratamento de erros HTTP
- Testes das rotas utilizando Swagger
- Validação da persistência após reiniciar o servidor

🎥 **Assista à Parte 02 — FastAPI + SQLite:**

https://youtube.com/live/Vk4B2gRAPLI

---

## 🛠️ Tecnologias utilizadas

- **Python 3** — Linguagem de programação
- **FastAPI** — Framework para construção da API REST
- **SQLite** — Banco de dados relacional
- **sqlite3** — Biblioteca nativa do Python para trabalhar com SQLite
- **Pydantic** — Definição e validação dos modelos de dados
- **Uvicorn** — Servidor para executar a aplicação
- **Swagger UI** — Documentação e testes interativos da API

O SQLite não exige a instalação de um servidor de banco de dados separado.

---

## ⚙️ Funcionalidades

- ✅ Listar todas as tarefas
- ✅ Criar uma nova tarefa
- ✅ Buscar uma tarefa pelo ID
- ✅ Atualizar uma tarefa existente
- ✅ Excluir uma tarefa
- ✅ Salvar os dados no SQLite
- ✅ Manter os registros após reiniciar o servidor
- ✅ Criar automaticamente a tabela de tarefas
- ✅ Retornar erro 404 quando uma tarefa não for encontrada
- ✅ Testar as operações pela documentação Swagger

---

## 🗄️ Estrutura do banco de dados

O projeto utiliza um banco SQLite chamado `tarefas.db`.

A tabela `tarefas` possui os seguintes campos:

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Identificador único, autoincremento |
| titulo | TEXT | Título da tarefa |
| descricao | TEXT | Descrição da tarefa |
| concluida | INTEGER | Estado da tarefa: 0 ou 1 |

O campo `concluida` representa um valor booleano:

- `0` — Tarefa não concluída
- `1` — Tarefa concluída

O banco e a tabela são criados automaticamente pela aplicação quando necessário.

---

## 🔗 Rotas da API

| Método | Rota | Descrição |
|---|---|---|
| GET | `/tarefas` | Lista todas as tarefas |
| POST | `/tarefas` | Cria uma nova tarefa |
| GET | `/tarefas/{tarefa_id}` | Busca uma tarefa pelo ID |
| PUT | `/tarefas/{tarefa_id}` | Atualiza uma tarefa |
| DELETE | `/tarefas/{tarefa_id}` | Remove uma tarefa |

### Principais códigos HTTP

| Código | Significado |
|---|---|
| 200 | Requisição realizada com sucesso |
| 201 | Tarefa criada com sucesso |
| 204 | Tarefa excluída com sucesso |
| 404 | Tarefa não encontrada |
| 422 | Dados da requisição inválidos |

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/marcoscaldas/ProjetoFastApiComPython.git
```

Entre na pasta do projeto:

```bash
cd ProjetoFastApiComPython
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows — PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Instale as dependências

Se o projeto possuir o arquivo `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Ou instale os pacotes necessários:

```bash
python -m pip install fastapi uvicorn
```

> A biblioteca `sqlite3` já faz parte da biblioteca padrão do Python e não precisa ser instalada separadamente.

### 5. Inicie o servidor

```bash
python -m uvicorn main:app --reload
```

A API estará disponível em:

http://localhost:8000

---

## 📖 Documentação interativa — Swagger

Com o servidor em execução, acesse:

**http://localhost:8000/docs**

Pelo Swagger você poderá:

- Cadastrar tarefas
- Consultar todas as tarefas
- Buscar tarefas pelo ID
- Atualizar informações
- Excluir registros
- Visualizar os códigos HTTP retornados pela API

---

## 📝 Exemplo de cadastro de tarefa

Na rota `POST /tarefas`, utilize o seguinte JSON:

```json
{
  "titulo": "Estudar FastAPI",
  "descricao": "Aprender persistência de dados com SQLite",
  "concluida": false
}
```

O identificador `id` será gerado automaticamente pelo banco de dados.

### Exemplo de resposta

```json
{
  "id": 1,
  "titulo": "Estudar FastAPI",
  "descricao": "Aprender persistência de dados com SQLite",
  "concluida": false
}
```

O valor do ID pode variar conforme os registros existentes no banco.

---

## 💾 Testando a persistência dos dados

Para verificar se a aplicação está salvando corretamente as tarefas:

1. Inicie o servidor.
2. Acesse o Swagger.
3. Cadastre uma tarefa utilizando POST.
4. Consulte as tarefas utilizando GET.
5. Pare o servidor.
6. Inicie o servidor novamente.
7. Execute o GET mais uma vez.

**Resultado esperado:** a tarefa cadastrada anteriormente continuará disponível, pois agora está armazenada no SQLite.

Essa é a principal evolução em relação à primeira versão do projeto.

---

## 🧠 Conceitos praticados

Durante o desenvolvimento, trabalhamos conceitos importantes para quem está aprendendo backend:

- API REST
- Métodos HTTP
- Códigos de status HTTP
- Modelagem de dados
- Persistência de informações
- Banco de dados relacional
- Consultas SQL
- Validação de dados
- Tratamento de erros
- Testes de endpoints
- Depuração e desenvolvimento incremental

---

## 🔜 Próximas evoluções

O projeto continuará evoluindo nas próximas aulas.

Uma das próximas etapas será organizar o código utilizando o padrão **MVC (Model, View e Controller)**, separando responsabilidades e melhorando a estrutura da aplicação.

A proposta é evoluir o mesmo projeto progressivamente, entendendo o motivo de cada mudança.

---

## 👨‍🏫 Desvendando o Código

Projeto desenvolvido pelo **Professor Marcos**, no canal **Desvendando o Código**.

Aqui você aprende programação de maneira prática, acompanhando o desenvolvimento de projetos reais e entendendo os conceitos por trás do código.

**Aprender a programar não é apenas copiar código. É entender o problema e construir a solução!**

🎥 YouTube: https://www.youtube.com/@desvendandoocodigo

🌐 Blog: https://desvendandoocodigo.com.br

---

⭐ Se este projeto ajudou nos seus estudos, deixe uma estrela no repositório e acompanhe as próximas evoluções!