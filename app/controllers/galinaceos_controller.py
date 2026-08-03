from flask import request
from flask_restful import Resource, marshal

from app.services.galinaceos_service import GalinaceosService
from app.schemas.galinaceos_fields import galinaceos_fields

class GalinaceosController(Resource):


    def get(self):
        filtros = {
            "SIST_CRIA": request.args.get("SIST_CRIA"),
            "NIV_TERR": request.args.get("NIV_TERR"),
            "COD_TERR": request.args.get("COD_TERR"),
            "NOM_TERR": request.args.get("NOM_TERR"),
            "CL_GAL": request.args.get("CL_GAL"),
        }

        resultado = GalinaceosService.buscar(filtros)
        return marshal(resultado, galinaceos_fields), 200