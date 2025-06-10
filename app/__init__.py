from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
import os

db = SQLAlchemy()
login_manager = LoginManager()
moment = Moment()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)

    # Import blueprints
    from .auth.routes import auth_bp
    from .main.routes import main_bp
    from .admin.routes import admin_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    return app
