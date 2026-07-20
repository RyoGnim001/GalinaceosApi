from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

from helpers.cors import cors

app = Flask(__name__)
api = Api(app)

cors.init_app(app)

# Load variables from .env into os.environ
load_dotenv()
