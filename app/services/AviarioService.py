from app.repositories.AviarioRepository import AviarioRepository


class AviarioService:

    def getAll(self):
        return AviarioRepository().getAll()

    def getById(self, aviario_id):
        return AviarioRepository().getById(aviario_id)

    def create(self, data):
        return AviarioRepository().create(data)

    def update(self, aviario_id, data):
        return AviarioRepository().update(aviario_id, data)

    def delete(self, aviario_id):
        return AviarioRepository().delete(aviario_id)