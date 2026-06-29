from app.repository.galinaceos_repository import GalinaceosRepository

class GalinaceosService:
    @staticmethod
    def buscar(filtros):
        return GalinaceosRepository.buscar(filtros)