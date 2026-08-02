from flask_restful import dto

avicultor_fields = {
    'id': dto.Integer,
    'nome': dto.String,
    'nascimento': dto.DateTime(dt_format='iso8601'),
    'cpf': dto.String,
    'caf': dto.String,
}

avicultor_id_fields = {
    'id': dto.Integer
}