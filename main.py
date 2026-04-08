from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from model import database_model
from routes.products_route import router as product_router

app = FastAPI()


NOT_FOUND = {"message": "Product Not found"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:3000"],
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"]
)

database_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Greet": "Welcome To my server"}


# 👇 register routes
app.include_router(product_router, prefix="/products", tags=["Products"])


# def init_db():
#    db = session()
#    count = db.query(database_model.Product_Model).count()
#    if count == 0:
#       for product in products:
#          db.add(database_model.Product_Model(**product.model_dump()))
#       db.commit()

# init_db()
