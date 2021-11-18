from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_restful import Api
#from flask_cors import CORS

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    #CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    Api(app, catch_all_404s=True)
    app.url_map.strict_slashes = False

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .services import services as services_blueprint
    app.register_blueprint(services_blueprint)

    return app
