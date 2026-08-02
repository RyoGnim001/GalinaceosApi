from marshmallow import Schema, fields, validate

class EnderecoSchema(Schema):
    logradouro = fields.Str(required=False, allow_none=True)
    cep = fields.Str(required=True, validate=validate.Length(
    equal=8, error="CEP deve ter 8 dígitos."), error_messages={"required": "Adicione um CEP."})
    numero = fields.Int(required=False, allow_none=True)
    avicultor_id = fields.Int(required=True, error_messages={"required": "Informe o avicultor."})
