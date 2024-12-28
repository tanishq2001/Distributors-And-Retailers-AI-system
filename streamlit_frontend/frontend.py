import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:5000"

st.title("GreenLife Foods Chatbot")

# Chat Interface
st.header("Chat with the bot")
message = st.text_input("Your message")
if st.button("Send"):
    response = requests.post(f"{BASE_URL}/chat", json={"message": message})
    bot_response = response.json().get("response", "Sorry, I couldn't process that.")
    st.write(f"Bot: {bot_response}")

# Product List
st.header("Products")
products_response = requests.get(f"{BASE_URL}/products")
# products = products_response.json()

# for product in products:
#     st.subheader(product['name'])
#     st.write(product['description'])
#     st.write(f"Price: ${product['price']}")
#     st.write(f"Stock: {product['stock']}")
#     quantity = st.number_input(f"Quantity to add for {product['name']}", min_value=1, max_value=product['stock'], step=1)
#     if st.button(f"Add {product['name']} to Cart"):
#         cart_response = requests.post(f"{BASE_URL}/cart", json={"product_id": product['id'], "quantity": quantity})
#         st.write(cart_response.json())

# # Cart Summary
# st.header("Cart Summary")
# st.write(cart_response.json() if 'cart_response' in locals() else "Cart is empty.")
