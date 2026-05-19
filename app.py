from helpers.application import app
from controllers.AvicultorController import avicultor_bp


@app.get("/")
def index():
    return '{"versao":"1.0.1"}', 200


@app.get("/health")
def healthCheck():
    return "{'online':'true'}", 200


app.register_blueprint(avicultor_bp)
