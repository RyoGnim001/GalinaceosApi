from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError

from app.schemas.avicula_schema import AviculaSchema
from app.schemas.avicula_fields import avicula_fields
from app.services.AviculaService import AviculaService
from app.helpers.logger import logger

CAMPOS_FILTRO = {"nome", "capacidade", "area", "avicultor_id"}


class AviculasController(Resource):

    def get(self):
        logger.info("Listando avículas")

        filtros = {
            k: v
            for k, v in request.args.items()
            if k in CAMPOS_FILTRO and v
        }

        aviculas = AviculaService().getAll(filtros)

        return marshal(aviculas, avicula_fields), 200

    def post(self):
        try:
            data = AviculaSchema().load(request.get_json())

            avicula = AviculaService().create(data)

            return marshal(avicula, avicula_fields), 201

        except ValidationError as err:
            return err.messages, 400


class AviculaController(Resource):

    def get(self, avicula_id):
        avicula = AviculaService().getById(avicula_id)

        if avicula is None:
            return {"mensagem": "Avícula não encontrada."}, 404

        return marshal(avicula, avicula_fields), 200

    def put(self, avicula_id):
        try:
            data = AviculaSchema().load(request.get_json())

            avicula = AviculaService().update(avicula_id, data)

            if avicula is None:
                return {"mensagem": "Avícula não encontrada."}, 404

            return marshal(avicula, avicula_fields), 200

        except ValidationError as err:
            return err.messages, 400

    def delete(self, avicula_id):

        removido = AviculaService().delete(avicula_id)

        if not removido:
            return {"mensagem": "Avícula não encontrada."}, 404

        return {"mensagem": "Avícula removida com sucesso."}, 200