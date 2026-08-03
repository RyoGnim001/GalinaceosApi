from flask import request, jsonify
from flask_restful import Resource, marshal
from marshmallow import ValidationError

from app.schemas.aviario_schema import AviarioSchema
from app.schemas.aviario_fields import aviario_fields
from app.services.AviarioService import AviarioService


class AviariosController(Resource):

    def get(self):
        return marshal(
            AviarioService().getAll(),
            aviario_fields
        ), 200

    def post(self):
        try:
            data = AviarioSchema().load(request.get_json())
            aviario = AviarioService().create(data)

            return marshal(aviario, aviario_fields), 201

        except ValidationError as err:
                return err.messages, 400


class AviarioController(Resource):

    def get(self, aviario_id):

        aviario = AviarioService().getById(aviario_id)

        if aviario is None:
            return {"mensagem": "Aviário não encontrado."}, 404

        return marshal(aviario, aviario_fields), 200

    def put(self, aviario_id):

        try:
            data = AviarioSchema().load(request.get_json())

            aviario = AviarioService().update(aviario_id, data)

            if aviario is None:
                return {"mensagem": "Aviário não encontrado."}, 404

            return marshal(aviario, aviario_fields), 200

        except ValidationError as err:
            return err.messages, 400

    def delete(self, aviario_id):

        removido = AviarioService().delete(aviario_id)

        if not removido:
            return {"mensagem": "Aviário não encontrado."}, 404

        return {"mensagem": "Aviário removido com sucesso."}, 200