from flask_restful import fields

aviario_fields = {
    "id": fields.Integer,
    "nome": fields.String,
    "capacidade": fields.Integer,
    "area": fields.Float,
    "avicula_id": fields.Integer,
}