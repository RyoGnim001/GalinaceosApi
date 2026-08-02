from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

from helpers.cors import cors
from helpers.database import db
from helpers.enviroment import enviroment

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{enviroment.get('DB_USER')}:"
    f"{enviroment.get('DB_PASSWORD')}@"
    f"{enviroment.get('DB_HOST')}:"
    f"{enviroment.get('DB_PORT')}/"
    f"{enviroment.get('DB_NAME')}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

db.init_app(app)

cors.init_app(app)

with app.app_context():
    db.create_all()