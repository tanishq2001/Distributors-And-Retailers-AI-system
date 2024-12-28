import requests
from app.models import Product, db

# Llama-3.1-8b API integration
def query_llama(prompt):
    url = "https://llama-api.example.com/v1/generate"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    data = {"prompt": prompt, "max_tokens": 200}
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("text", "")

def get_products():
    products = Product.query.all()
    return [p.to_dict() for p in products]

def add_to_cart(cart, product_id, quantity):
    product = Product.query.get(product_id)
    if not product or product.stock < quantity:
        return {"error": "Product unavailable or insufficient stock."}
    product.stock -= quantity
    db.session.commit()
    cart.append({"product": product.to_dict(), "quantity": quantity})
    return cart
