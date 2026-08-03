from app.repositories.GalinaceosRepository import GalinaceosRepository

class GalinaceosService:
    @staticmethod
    def buscar(filtros):
        return GalinaceosRepository.buscar(filtros)