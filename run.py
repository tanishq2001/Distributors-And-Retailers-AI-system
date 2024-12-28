from app import create_app
from app.models import db, Product

app = create_app()

# Seeding database
@app.before_first_request
def seed_database():
    db.create_all()
    if not Product.query.first():
        products = [
            {"name": "Apple Juice", "description": "Fresh organic apple juice.", "price": 3.5, "stock": 100},
            {"name": "Orange Juice", "description": "Pure organic orange juice.", "price": 4.0, "stock": 80}
            # Add more products here
        ]
        for product in products:
            db.session.add(Product(**product))
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
