from flask import Flask
from app.models import db
from app.views import views  # Import the blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/products.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    # Register the blueprint
    app.register_blueprint(views, url_prefix="/")
    
    return app
