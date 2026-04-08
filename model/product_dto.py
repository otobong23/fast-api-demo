from pydantic import BaseModel


class Product_Update(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
