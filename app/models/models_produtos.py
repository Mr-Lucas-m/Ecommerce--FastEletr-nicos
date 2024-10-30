#app/models/models_produtos.py

from sqlalchemy import Column, Integer, String, Float
from app.database.indb import Base

#define a estrutura da tabela no banco de dados
class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # ID auto-incrementável
    nome = Column(String, index=True)
    preco = Column(Float)
    descricao = Column(String)



