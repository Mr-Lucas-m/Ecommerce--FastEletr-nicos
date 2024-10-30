#app/database/indb.py

import os
from sqlalchemy import create_engine
from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker
from dotenv import load_dotenv

#carrega variaveis do .env
load_dotenv()

#puxa a url do banco dedos
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"database_url: {DATABASE_URL}")
#cria a conexão com o BD
conexao_pg = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=conexao_pg)
Base = declarative_base()

def obter_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()     

def init_db():
    from app.models import models_produtos
    Base.metadata.create_all(bind=conexao_pg)    #cria todas as tabelas do banco de dados 


