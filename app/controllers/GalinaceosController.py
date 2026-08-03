from flask import request
from flask_restful import Resource, marshal

from app.services.GalinaceosService import GalinaceosService
from app.schemas.galinaceos_fields import galinaceos_fields


class GalinaceosController(Resource):

    def get(self):

        cl_gal = request.args.get("CL_GAL")

        if cl_gal is not None:
            try:
                int(cl_gal)
            except ValueError:
                return {
                    "mensagem": "O parâmetro CL_GAL deve ser um número inteiro."
                }, 400

        filtros = {
            "SIST_CRIA": request.args.get("SIST_CRIA"),
            "NIV_TERR": request.args.get("NIV_TERR"),
            "COD_TERR": request.args.get("COD_TERR"),
            "NOM_TERR": request.args.get("NOM_TERR"),
            "CL_GAL": cl_gal,
        }

        resultado = GalinaceosService.buscar(filtros)

        return marshal(resultado, galinaceos_fields), 200