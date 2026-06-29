from app.helpers.database import db
from app.models.galinaceos import Galinaceos
from app.models.sistema_criacao import SistemaCriacao
from app.models.territorio import Territorio
from app.models.classe_galinaceos import ClasseGalinaceos

class GalinaceosRepository:
    @staticmethod
    def buscar(filtros):
        query = db.session.query(Galinaceos)\
            .join(SistemaCriacao, Galinaceos.sist_cria_id == SistemaCriacao.id)\
            .join(Territorio, Galinaceos.territorio_id == Territorio.id)\
            .join(ClasseGalinaceos, Galinaceos.cl_gal_id == ClasseGalinaceos.id)

        if filtros.get("SIST_CRIA"):
            query = query.filter(SistemaCriacao.codigo == filtros["SIST_CRIA"])

        if filtros.get("NIV_TERR"):
            query = query.filter(Territorio.nivel_territorial == filtros["NIV_TERR"])

        if filtros.get("COD_TERR"):
            query = query.filter(Territorio.codigo_territorio == filtros["COD_TERR"])

        if filtros.get("NOM_TERR"):
            query = query.filter(Territorio.nome_territorio == filtros["NOM_TERR"])

        if filtros.get("CL_GAL"):
            query = query.filter(ClasseGalinaceos.codigo == int(filtros["CL_GAL"]))

        return query.all()