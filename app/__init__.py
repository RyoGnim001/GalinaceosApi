from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from .helpers.database import init_db
from .helpers.application import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    init_db(app)
    register_blueprints(app)

    return app