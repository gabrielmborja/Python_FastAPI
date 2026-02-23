# API FastAPI – CRUD de Usuário com Perfil

API desenvolvida com FastAPI utilizando SQLAlchemy como ORM.
Implementa um CRUD completo de Usuário com relacionamento 1:1 com Perfil.

Projeto acadêmico com foco em utilização de ORM em APIs backend.

Tecnologias

a) Python                                             
b) FastAPI                                   
c) SQLAlchemy                              
d) SQLite                              
e) Uvicorn

# Como fazemos para rodarmos esse projeto

Criar ambiente virtual

python -m venv venv
venv\Scripts\activate

Instalar dependências

pip install fastapi uvicorn sqlalchemy

Executar a aplicação

uvicorn main:app --reload

A API ficará disponível em:

http://127.0.0.1:8000

Documentação interativa (Swagger):

http://127.0.0.1:8000/docs
Funcionalidades

a) Criar usuário com perfil                                 
b) Listar usuários com perfil                                    
c) Atualizar usuário                                      
d) Deletar usuário                                                       
e) Validação de email duplicado

# Banco de Dados:

Utiliza SQLite, gerado automaticamente no arquivo test.db
