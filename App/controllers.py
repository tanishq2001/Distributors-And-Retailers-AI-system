import requests
from app.models import Product, db

# Llama-3.1-8b API integration
def query_llama(prompt):
    url = "https://llama-api.example.com/v1/generate"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    data = {"prompt": prompt, "max_tokens": 200}
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("text", "")

def process_chat_query(message, cart):
    """
    Process user chat queries and return a contextual response.
    """
    # Example prompt for Llama
    prompt = (
        f"You are a chatbot for an organic food company. You can only assist users in ordering from the following products:\n"
        f"{[p.name for p in Product.query.all()]}\n"
        f"User's Message: {message}\n"
        f"Respond with product suggestions, order details, or guidance."
    )
    response = query_llama(prompt)

    # Basic intent and entity extraction (can be enhanced)
    if "add" in message.lower():
        # Extract product and quantity (simple regex or NLP could be used)
        for product in Product.query.all():
            if product.name.lower() in message.lower():
                quantity = 1  # Default to 1
                words = message.split()
                for word in words:
                    if word.isdigit():
                        quantity = int(word)
                        break
                return add_to_cart(cart, product.id, quantity)
        return {"error": "Product not found in catalog. Please try again."}
    elif "view" in message.lower() or "show" in message.lower():
        return {"products": get_products()}
    else:
        return {"response": response}

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
