from helpers.application import app, api
from helpers.database import db

# Avicultor
from app.controllers.AvicultorController import (
    AvicultoresController,
    AvicultorController
)

from app.controllers.EnderecoController import (
    EnderecosController,
    EnderecoController
)

# Galináceos
from app.controllers.GalinaceosController import (
    GalinaceosController
)

from app.controllers.GalpaoController import (
    GalpoesController,
    GalpaoController
)

from app.controllers.AvicolaController import (
    AvicolasController,
    AvicolaController
)

from controllers.IndexController import (
    IndexController,
    HealthController
)

api.add_resource(IndexController, "/")
api.add_resource(HealthController, "/health")

api.add_resource(AvicultoresController, "/avicultores")
api.add_resource(AvicultorController, "/avicultores/<int:avicultor_id>")

api.add_resource(EnderecosController, "/enderecos")
api.add_resource(EnderecoController, "/enderecos/<int:endereco_id>")

api.add_resource(GalinaceosController, "/galinaceos")
api.add_resource(GalpoesController, "/galpoes")
api.add_resource(GalpaoController, "/galpoes/<int:galpao_id>")

api.add_resource(AvicolasController, "/avicola")
api.add_resource(AvicolaController, "/avicola/<int:avicola_id>")

with app.app_context():
    db.create_all()