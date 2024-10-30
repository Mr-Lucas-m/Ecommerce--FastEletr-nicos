#app/schemas/schemas_produtos.py
from pydantic import BaseModel

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    descricao: str

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float
    descricao: str

    class Config:
        from_attributes= True 
