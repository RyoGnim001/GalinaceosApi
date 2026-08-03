from app.helpers.database import db
from app.models.Aviario import Aviario


class AviarioRepository:

    def getAll(self):
        return db.session.query(Aviario).all()

    def getById(self, aviario_id):
        return db.session.get(Aviario, aviario_id)

    def create(self, data):
        aviario = Aviario(**data)

        db.session.add(aviario)
        db.session.commit()

        return aviario

    def update(self, aviario_id, data):

        aviario = db.session.get(Aviario, aviario_id)

        if aviario is None:
            return None

        for campo, valor in data.items():
            setattr(aviario, campo, valor)

        db.session.commit()

        return aviario

    def delete(self, aviario_id):

        aviario = db.session.get(Aviario, aviario_id)

        if aviario is None:
            return False

        db.session.delete(aviario)
        db.session.commit()

        return True