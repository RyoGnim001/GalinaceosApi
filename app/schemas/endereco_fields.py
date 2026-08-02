from flask_restful import dto

endereco_fields = {
    'id': dto.Integer,
    'logradouro': dto.String,
    'cep': dto.String,
    'numero': dto.Integer,
    'avicultor_id': dto.Integer,
}

endereco_id_fields = {
    'id': dto.Integer
}