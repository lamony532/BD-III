#git add .

#git commit -m "Estrutura inicial do projeto"

#git push

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

db_user = "aluno"
db_password = "aluno_senha"
db_name = "meu_banco_senai"
db_host = "localhost"
db_port = "3306"

#Endereço (URL) para conexão com banco de dados.
DATABASE_URL = f"mysql+pymysql://{db_user}: {db_password}@{db_host}:{db_port}/{db_name}"

#Criando banco de dados.
Session = sessionmaker(bind=db)
Session = Session()

#Gerenciando conexão com banco de dados.
@contextmanager
def get_db():
    db = Session()
    try:
        yield db #realiza tentativa de operação no BD.
        db.commit() #Salvando no BD
    except Exception as erro: 
        db.rollback() #Caso ocorra algum erro, desfazer alterações no BD.
        raise erro #Caso ocorra algum erro, mostrar mensagem no erro no terminal
    finally:
        db.close() #Fecha conexão com BD.