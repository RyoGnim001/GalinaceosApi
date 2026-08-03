from marshmallow import Schema, fields, validate


class GalpaoSchema(Schema):

    nome = fields.Str(
        required=True,
        error_messages={
            "required": "Adicione um nome."
        }
    )

    capacidade = fields.Int(
        required=True,
        validate=validate.Range(min=1),
        error_messages={
            "required": "Adicione a capacidade.",
            "invalid": "A capacidade deve ser um número inteiro."
        }
    )

    area = fields.Float(
        required=True,
        validate=validate.Range(min=0),
        error_messages={
            "required": "Adicione a área.",
            "invalid": "A área deve ser um número."
        }
    )

    avicula_id = fields.Int(
        required=True,
        error_messages={
            "required": "Informe a avícula."
        }
    )