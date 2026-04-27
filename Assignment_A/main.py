# main.py
# Install:
# pip install fastapi uvicorn pymongo

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()

# CORS for HTML frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["shopdb"]
collection = db["products"]


# Product Model
class Product(BaseModel):
    name: str
    price: float
    quantity: int


# Convert MongoDB Data
def product_data(data):
    return {
        "id": str(data["_id"]),
        "name": data["name"],
        "price": data["price"],
        "quantity": data["quantity"]
    }


# CREATE
@app.post("/products")
def create_product(product: Product):
    result = collection.insert_one(product.dict())
    return {
        "message": "Product Added",
        "id": str(result.inserted_id)
    }


# READ ALL
@app.get("/products")
def get_products():
    products = []
    for item in collection.find():
        products.append(product_data(item))
    return products


# READ ONE
@app.get("/products/{id}")
def get_product(id: str):
    item = collection.find_one({"_id": ObjectId(id)})

    if item:
        return product_data(item)

    raise HTTPException(status_code=404, detail="Product Not Found")


# UPDATE
@app.put("/products/{id}")
def update_product(id: str, product: Product):
    result = collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": product.dict()}
    )

    if result.modified_count == 1:
        return {"message": "Product Updated"}

    raise HTTPException(status_code=404, detail="Product Not Found")


# DELETE
@app.delete("/products/{id}")
def delete_product(id: str):
    result = collection.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 1:
        return {"message": "Product Deleted"}

    raise HTTPException(status_code=404, detail="Product Not Found")