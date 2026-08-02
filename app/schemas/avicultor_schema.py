from marshmallow import Schema, fields, validate

class AvicultorSchema(Schema):
    nome = fields.Str(required=True)
    nascimento = fields.Date(required=True)
    cpf = fields.Str(required=True, validate=validate.Length(max=11))
    caf = fields.Str(required=True)