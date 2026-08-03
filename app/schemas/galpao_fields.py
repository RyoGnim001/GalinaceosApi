from flask_restful import fields

galpao_fields = {
    "id": fields.Integer,
    "nome": fields.String,
    "capacidade": fields.Integer,
    "area": fields.Float,
    "avicula_id": fields.Integer,
}

galpao_id_fields = {
    "id": fields.Integer
}