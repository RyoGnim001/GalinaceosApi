from app.repositories.AviculaRepository import AviculaRepository


class AviculaService:

    def getAll(self, filtros):
        return AviculaRepository().getAll(filtros)

    def getById(self, avicula_id):
        return AviculaRepository().getById(avicula_id)

    def create(self, data):
        return AviculaRepository().create(data)

    def update(self, avicula_id, data):
        return AviculaRepository().update(avicula_id, data)

    def delete(self, avicula_id):
        return AviculaRepository().delete(avicula_id)