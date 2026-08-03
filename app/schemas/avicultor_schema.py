from marshmallow import Schema, fields

class AvicultorSchema(Schema):
    nome = fields.String(required=True)
    nascimento = fields.Date(required=True)
    cpf = fields.String(required=True)
    caf = fields.String(required=True)