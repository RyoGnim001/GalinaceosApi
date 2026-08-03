from app.helpers.application import app, api
from app.helpers.database import db
from flasgger import Swagger

Swagger(app)

# Controllers
from app.controllers.IndexController import (
    IndexController,
    HealthController
)

from app.controllers.AvicultorController import (
    AvicultoresController,
    AvicultorController
)

from app.controllers.EnderecoController import (
    EnderecosController,
    EnderecoController
)   

from app.controllers.AviculaController import (
    AviculasController,
    AviculaController
)

from app.controllers.AviarioController import (
    AviariosController,
    AviarioController
)

from app.controllers.GalpaoController import (
    GalpoesController,
    GalpaoController
)

from app.controllers.GalinaceosController import (
    GalinaceosController
)

# Models
from app.models.Avicultor import Avicultor
from app.models.Endereco import Endereco
from app.models.Avicula import Avicula
from app.models.Aviario import Aviario
from app.models.Galpao import Galpao

from app.models.galinaceos import Galinaceos
from app.models.classe_galinaceos import ClasseGalinaceos
from app.models.sistema_criacao import SistemaCriacao
from app.models.territorio import Territorio

# ============================
# Rotas Gerais
# ============================

api.add_resource(IndexController, "/") #ok
api.add_resource(HealthController, "/health")

# ============================
# Avicultor
# ============================

api.add_resource(AvicultoresController, "/avicultores") #ok
api.add_resource(AvicultorController, "/avicultores/<int:avicultor_id>")

# ============================
# Endereço
# ============================

api.add_resource(EnderecosController, "/enderecos") #ok
api.add_resource(EnderecoController, "/enderecos/<int:endereco_id>")

# ============================
# Avícola
# ============================

api.add_resource(AviculasController, "/avicola") #ok
api.add_resource(AviculaController, "/avicola/<int:avicola_id>")

# ============================
# Aviário
# ============================

api.add_resource(AviariosController, "/aviarios") #ok
api.add_resource(AviarioController, "/aviarios/<int:aviario_id>")

# ============================
# Galpão
# ============================

api.add_resource(GalpoesController, "/galpoes") #ok
api.add_resource(GalpaoController, "/galpoes/<int:galpao_id>")

# ============================
# Galináceos
# ============================

api.add_resource(GalinaceosController, "/galinaceos") #ok

# ============================
# Criação das tabelas
# ============================

with app.app_context():
    db.create_all()

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)