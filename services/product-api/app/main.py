from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Clixx Commerce Product API",
    version="0.1.0"
)


class Product(BaseModel):
    id: int
    name: str
    price: float
    inventory: int


products = [
    Product(id=1, name="Running Shoes", price=89.99, inventory=25),
    Product(id=2, name="Training Jacket", price=64.99, inventory=15),
    Product(id=3, name="Athletic Leggings", price=49.99, inventory=30),
]


@app.get("/health/live")
def liveness():
    return {"status": "alive"}


@app.get("/products", response_model=list[Product])
def list_products():
    return products


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
