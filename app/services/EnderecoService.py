from app.repositories.EnderecoRepository import EnderecoRepository
from app.repositories.AvicultorRepository import AvicultorRepository
from app.helpers.logger import logger


class EnderecoService:

    def __init__(self):
        self.enderecoRepository = EnderecoRepository()
        self.avicultorRepository = AvicultorRepository()

    def getAll(self, filtros=None):
        return self.enderecoRepository.getAll(filtros)

    def getByIdEndereco(self, id):
        return self.enderecoRepository.getByIdEndereco(id)

    def _validarAvicultor(self, avicultor_id):
        avicultor = self.avicultorRepository.getByIdAvicultor(avicultor_id)

        if avicultor is None:
            raise Exception("Avicultor não encontrado.")

    def create(self, data):

        self._validarAvicultor(data["avicultor_id"])

        endereco = self.enderecoRepository.insert(
            data.get("logradouro"),
            data["cep"],
            data.get("numero"),
            data["avicultor_id"]
        )

        logger.info(f"Endereço criado com id: {endereco.id}")

        return endereco

    def update(self, id, data):

        self._validarAvicultor(data["avicultor_id"])

        return self.enderecoRepository.update(
            id,
            data.get("logradouro"),
            data["cep"],
            data.get("numero"),
            data["avicultor_id"]
        )

    def delete(self, id):
        return self.enderecoRepository.delete(id)