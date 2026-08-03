from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError

from app.schemas.galpao_schema import GalpaoSchema
from app.schemas.galpao_fields import galpao_fields
from app.services.GalpaoService import GalpaoService
from app.helpers.logger import logger

CAMPOS_FILTRO = {"nome", "capacidade", "area", "avicula_id"}


class GalpoesController(Resource):

    def get(self):
        logger.info("Listando galpões")

        filtros = {
            k: v
            for k, v in request.args.items()
            if k in CAMPOS_FILTRO and v
        }

        galpoes = GalpaoService().getAll(filtros)

        return marshal(galpoes, galpao_fields), 200

    def post(self):
        try:
            data = GalpaoSchema().load(request.get_json())

            galpao = GalpaoService().create(data)

            return marshal(galpao, galpao_fields), 201

        except ValidationError as err:
            return jsonify(err.messages), 400


class GalpaoController(Resource):

    def get(self, galpao_id):

        galpao = GalpaoService().getById(galpao_id)

        if galpao is None:
            return {"mensagem": "Galpão não encontrado."}, 404

        return marshal(galpao, galpao_fields), 200

    def put(self, galpao_id):

        try:
            data = GalpaoSchema().load(request.get_json())

            galpao = GalpaoService().update(galpao_id, data)

            if galpao is None:
                return {"mensagem": "Galpão não encontrado."}, 404

            return marshal(galpao, galpao_fields), 200

        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, galpao_id):

        removido = GalpaoService().delete(galpao_id)

        if not removido:
            return {"mensagem": "Galpão não encontrado."}, 404

        return {"mensagem": "Galpão removido com sucesso."}, 200