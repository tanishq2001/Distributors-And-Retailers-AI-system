from flask import Blueprint, request, jsonify
from app.controllers import query_llama, get_products, add_to_cart

views = Blueprint('views', __name__)

cart = []

@views.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = query_llama(user_message)
    return jsonify({"response": response})

@views.route("/products", methods=["GET"])
def products():
    return jsonify(get_products())

@views.route("/cart", methods=["POST"])
def cart_handler():
    product_id = request.json.get("product_id")
    quantity = request.json.get("quantity", 1)
    result = add_to_cart(cart, product_id, quantity)
    return jsonify(result)
