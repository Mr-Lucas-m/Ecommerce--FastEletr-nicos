#app/crud/crud_produtos.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models import models_produtos
from app.models.models_produtos import Produto
from app.schemas.schemas_produtos import ProdutoCreate

#função que adciona/cria produtos no banco de dados
def criar_produto(db: Session, produto: ProdutoCreate):
      novo_produto = Produto(nome=produto.nome, preco=produto.preco, descricao=produto.descricao)
      db.add(novo_produto)
      db.commit()
      db.refresh(novo_produto)
      return novo_produto


#lista todos os produtos da tabela produtos
def lista_de_produtos(db: Session):
    return db.query(models_produtos.Produto).all()

#deleta poroduto do banco de dados
def deletar_produto(db: Session, produto_id: int):
        produtoDeletar = db.query(Produto).filter(Produto.id == produto_id).first()

        if not produtoDeletar:
             raise HTTPException(
                  status_code=status.HTTP_404_NOT_FOUND,
                  detail=f"Produto com id {produto_id} não encontrado."
             )
        db.delete(produtoDeletar)
        db.commit()

        return {"msg": f"Produto com id {produto_id} foi deletado com sucesso!"}