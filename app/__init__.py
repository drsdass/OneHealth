
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
import os

db = SQLAlchemy()
login_manager = LoginManager()
moment = Moment()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("FLASK_SECRET_KEY", "devkey"),
        SQLALCHEMY_DATABASE_URI='sqlite:///portal.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)

    login_manager.login_view = 'auth.login'

    from .auth.routes import auth_bp
    from .admin.routes import admin_bp
    from .main.routes import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app
