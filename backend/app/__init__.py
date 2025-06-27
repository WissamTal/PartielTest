from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import os

db = SQLAlchemy()
jwt = JWTManager()
load_dotenv()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cinecampus.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.film_routes import film_bp
    from app.routes.review_routes import review_bp

    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(film_bp, url_prefix='/api/films')
    app.register_blueprint(review_bp, url_prefix='/api/films')

    return app