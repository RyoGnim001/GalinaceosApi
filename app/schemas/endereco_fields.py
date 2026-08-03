from flask_restful import fields

endereco_fields = {
    'id': fields.Integer,
    'logradouro': fields.String,
    'cep': fields.String,
    'numero': fields.Integer,
    'avicultor_id': fields.Integer,
}

endereco_id_fields = {
    'id': fields.Integer
}