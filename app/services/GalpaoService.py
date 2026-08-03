from app.repositories.GalpaoRepository import GalpaoRepository


class GalpaoService:

    def getAll(self, filtros):
        return GalpaoRepository().getAll(filtros)

    def getById(self, galpao_id):
        return GalpaoRepository().getById(galpao_id)

    def create(self, data):
        return GalpaoRepository().create(data)

    def update(self, galpao_id, data):
        return GalpaoRepository().update(galpao_id, data)

    def delete(self, galpao_id):
        return GalpaoRepository().delete(galpao_id)