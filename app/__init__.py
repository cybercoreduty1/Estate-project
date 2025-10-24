from flask import Flask
from.extensions import db, migrate,login_manager
from .config import Config
from .routes.main_routes import bp as main_pb

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)

    app.register_blueprint(main_pb)
    #app.register_blueprint(auth_bp, url_prefix="/auth")

    return app