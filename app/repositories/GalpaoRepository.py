from app.helpers.database import db
from app.models.Galpao import Galpao


class GalpaoRepository:

    def getAll(self, filtros):

        query = db.session.query(Galpao)

        if filtros.get("nome"):
            query = query.filter(
                Galpao.nome.ilike(f"%{filtros['nome']}%")
            )

        if filtros.get("capacidade"):
            query = query.filter(
                Galpao.capacidade == int(filtros["capacidade"])
            )

        if filtros.get("area"):
            query = query.filter(
                Galpao.area == float(filtros["area"])
            )

        if filtros.get("avicula_id"):
            query = query.filter(
                Galpao.avicula_id == int(filtros["avicula_id"])
            )

        return query.all()

    def getById(self, galpao_id):
        return db.session.get(Galpao, galpao_id)

    def create(self, data):

        galpao = Galpao(**data)

        db.session.add(galpao)
        db.session.commit()

        return galpao

    def update(self, galpao_id, data):

        galpao = db.session.get(Galpao, galpao_id)

        if galpao is None:
            return None

        for chave, valor in data.items():
            setattr(galpao, chave, valor)

        db.session.commit()

        return galpao

    def delete(self, galpao_id):

        galpao = db.session.get(Galpao, galpao_id)

        if galpao is None:
            return False

        db.session.delete(galpao)
        db.session.commit()

        return True