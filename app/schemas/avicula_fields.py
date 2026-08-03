from flask_restful import fields

avicula_fields = {
    "id": fields.Integer,
    "nome": fields.String,
    "capacidade": fields.Integer,
    "area": fields.Float,
    "avicultor_id": fields.Integer,
}

avicula_id_fields = {
    "id": fields.Integer
}