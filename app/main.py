#app/main.py

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database.indb import obter_db, init_db
from app.crud import crud_produtos
from app.schemas import schemas_produtos
from app.schemas.schemas_produtos import ProdutoResponse, ProdutoCreate
app = FastAPI()

#configuração do CORS, permite que o frontend faça requisições 
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"], #URL do frontend react
    allow_credentials = True,
    allow_methods = ["*"],
    allow_header = ["*"],
)

@app.on_event("startup")
def on_event():
    init_db()


#Criação de um novo produto    
@app.post("/criarProduto", response_model=ProdutoResponse)
async def criar_produto(produto: ProdutoCreate, db: Session=Depends(obter_db)):
    return crud_produtos.criar_produto(db, produto)


#Rota que lista os produtos do banco de dados
@app.get("/listaProdutos", response_model=list[schemas_produtos.ProdutoResponse])
def listao_de_produtos(db: Session = Depends(obter_db)):
    return crud_produtos.lista_de_produtos(db)


#Rota que deleta produtos
@app.delete("/deletarProduto/{produto_id}")
async def deletar_produto(produto_id: int, db: Session = Depends(obter_db)):
    return crud_produtos.deletar_produto(db, produto_id)