from app.models.Avicula import Avicula
from app.helpers.database import db


class AviculaRepository:

    def getAll(self, filtros):

        query = db.session.query(Avicula)

        if filtros.get("nome"):
            query = query.filter(
                Avicula.nome.ilike(f"%{filtros['nome']}%")
            )

        if filtros.get("capacidade"):
            query = query.filter(
                Avicula.capacidade == int(filtros["capacidade"])
            )

        if filtros.get("area"):
            query = query.filter(
                Avicula.area == float(filtros["area"])
            )

        if filtros.get("avicultor_id"):
            query = query.filter(
                Avicula.avicultor_id == int(filtros["avicultor_id"])
            )

        return query.all()

    def getById(self, avicula_id):
        return db.session.get(Avicula, avicula_id)

    def create(self, data):

        avicula = Avicula()

        avicula.nome = data["nome"]
        avicula.capacidade = data["capacidade"]
        avicula.area = data["area"]
        avicula.avicultor_id = data["avicultor_id"]

        db.session.add(avicula)
        db.session.commit()

        return avicula

    def update(self, avicula_id, data):

        avicula = db.session.get(Avicula, avicula_id)

        if avicula is None:
            return None

        avicula.nome = data["nome"]
        avicula.capacidade = data["capacidade"]
        avicula.area = data["area"]
        avicula.avicultor_id = data["avicultor_id"]

        db.session.commit()

        return avicula

    def delete(self, avicula_id):

        avicula = db.session.get(Avicula, avicula_id)

        if avicula is None:
            return False

        db.session.delete(avicula)
        db.session.commit()

        return True