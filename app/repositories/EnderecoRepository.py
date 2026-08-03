from sqlalchemy import select

from app.helpers.database import db
from app.helpers.logger import logger
from app.models.Endereco import Endereco


class EnderecoRepository:

    def getAll(self, filtros=None):
        stmt = select(Endereco)

        if filtros:
            stmt = stmt.filter_by(**filtros)

        return db.session.execute(stmt).scalars().all()

    def getByIdEndereco(self, id):
        logger.info("Consultando endereço pelo id.")
        return db.session.get(Endereco, id)

    def insert(self, logradouro, cep, numero, avicultor_id):

        endereco = Endereco()

        endereco.logradouro = logradouro
        endereco.cep = cep
        endereco.numero = numero
        endereco.avicultor_id = avicultor_id

        db.session.add(endereco)
        db.session.commit()

        logger.info(f"Endereço inserido com id: {endereco.id}")

        return endereco

    def update(self, id, logradouro, cep, numero, avicultor_id):

        endereco = db.session.get(Endereco, id)

        if endereco is None:
            return None

        endereco.logradouro = logradouro
        endereco.cep = cep
        endereco.numero = numero
        endereco.avicultor_id = avicultor_id

        db.session.commit()

        return endereco

    def delete(self, id):

        endereco = db.session.get(Endereco, id)

        if endereco is None:
            return False

        db.session.delete(endereco)
        db.session.commit()

        return True