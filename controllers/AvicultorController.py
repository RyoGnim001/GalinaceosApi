from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from models.Avicultor import AvicultorSchema
from services.AvicultoresService import AvilcultorService
from helpers.logger import logger

avicultor_bp = Blueprint('avicultor', __name__, url_prefix='/avicultores')


@avicultor_bp.get("/")
def getAvicultores():
    # nome, cpf, caf
    logger.info("Listando todos os avicultores")
    all_params_dictionary = request.args.to_dict()
    print("Estrutura dos parametros")
    print(all_params_dictionary)

    meu_dicionario = {'nome': 'Maria', 'cpf': '111', 'caf': '1010'}
    for key, value in meu_dicionario.items():
        print(f"Chave: {key}")
        print(f"Valor: {value}")
    # nome = request.args.get("nome")
    # cpf = request.args.get("cpf")
    # caf = request.args.get("caf")
    # avicultores = AvilcultorService().getAll(nome, cpf, caf)

    # return [a.toDict() for a in avicultores], 200

    return '', 200


@avicultor_bp.get("/<int:id>")
def getByIdAvicultores(id: int):
    logger.info(f"Listando avicultor pelo id: {id}")
    avicultor = AvilcultorService().getByIdAvicultor(id)
    if avicultor is None:
        return {"mensagem": "O avicultor não foi encontrado"}, 404
    return avicultor.toDict(), 200


@avicultor_bp.post("/")
def postAvicultores():
    try:
        data = AvicultorSchema().load(request.get_json())
        avicultor = AvilcultorService().create(data)
        return avicultor.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400


@avicultor_bp.put("/<int:id>")
def putAvicultores(id: int):
    try:
        data = AvicultorSchema().load(request.get_json())
        avicultor = AvilcultorService().update(id, data)
        if avicultor is None:
            return {"mensagem": "O avicultor não foi encontrado"}, 404
        return avicultor.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400


@avicultor_bp.delete("/<int:id>")
def deleteAvicultores(id: int):
    logger.info(f"Removendo avicultor id: {id}")
    removido = AvilcultorService().delete(id)
    if not removido:
        return {"mensagem": "O avicultor não foi encontrado"}, 404
    return {"mensagem": "Avicultor removido com sucesso!"}, 200
