from marshmallow import Schema, fields, validate


class AviarioSchema(Schema):

    nome = fields.Str(required=True)

    capacidade = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    area = fields.Float(
        required=True,
        validate=validate.Range(min=0)
    )

    avicula_id = fields.Int(required=True)