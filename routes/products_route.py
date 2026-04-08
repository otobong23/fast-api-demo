from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import session
from model.product_dto import Product_Update
from model import database_model

router = APIRouter()

NOT_FOUND = {"message": "Product Not found"}


def get_db():
   db = session()
   try:
      yield db
   finally:
      db.close()


@router.get("/")
def get_product(db: Session = Depends(get_db)):
   return db.query(database_model.Product_Model).all()


@router.get("/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
   db_product = (
      db.query(database_model.Product_Model)
      .filter(database_model.Product_Model.id == id)
      .first()
   )

   if not db_product:
      return NOT_FOUND

   return {"data": db_product}


@router.post("/")
def add_product(product: Product_Update, db: Session = Depends(get_db)):
    new_product = database_model.Product_Model(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {"data": new_product}


@router.put("/{id}")
def update_product(id: int, product: Product_Update, db: Session = Depends(get_db)):
   db_product = (
      db.query(database_model.Product_Model)
      .filter(database_model.Product_Model.id == id)
      .first()
   )

   if not db_product:
      return NOT_FOUND

   for key, value in product.model_dump().items():
      setattr(db_product, key, value)

   db.commit()
   db.refresh(db_product)

   return {"data": db_product, "message": "product updated successfully"}


@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
   db_product = (
      db.query(database_model.Product_Model)
      .filter(database_model.Product_Model.id == id)
      .first()
   )

   if not db_product:
      return NOT_FOUND

   db.delete(db_product)
   db.commit()

   return {"data": db_product, "message": "product deleted successfully"}
