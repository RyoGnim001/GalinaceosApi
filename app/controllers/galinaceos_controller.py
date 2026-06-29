from flask import Blueprint, request, jsonify
from app.services.galinaceos_service import GalinaceosService
from app.schemas.galinaceos_schema import GalinaceosSchema

bp = Blueprint("galinaceos", __name__, url_prefix="/galinaceos")
schema = GalinaceosSchema(many=True)

@bp.get("/")
def listar():
    filtros = {
        "SIST_CRIA": request.args.get("SIST_CRIA"),
        "NIV_TERR": request.args.get("NIV_TERR"),
        "COD_TERR": request.args.get("COD_TERR"),
        "NOM_TERR": request.args.get("NOM_TERR"),
        "CL_GAL": request.args.get("CL_GAL"),
    }

    resultado = GalinaceosService.buscar(filtros)
    return jsonify(schema.dump(resultado)), 200