from helpers.application import app, api
from controllers.AvicultorController import AvicultoresController, AvicultorController
from controllers.IndexController import IndexController, HealthController

# app.register_blueprint(index_bp)
api.add_resource(IndexController, '/')
api.add_resource(HealthController, '/health')


# app.register_blueprint(avicultor_bp)
api.add_resource(AvicultoresController, "/avicultores")
api.add_resource(AvicultorController, "/avicultores/<int:avicultor_id>")
