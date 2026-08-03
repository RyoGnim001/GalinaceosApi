from flask_restful import fields

avicultor_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'nascimento': fields.DateTime(dt_format='iso8601'),
    'cpf': fields.String,
    'caf': fields.String,
}

avicultor_id_fields = {
    'id': fields.Integer
}