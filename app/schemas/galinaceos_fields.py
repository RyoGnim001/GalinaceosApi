from flask_restful import fields

galinaceos_fields = {
    "id": fields.Integer,

    # Sistema de Criação
    "sist_cria": fields.String(attribute="sistema_criacao.codigo"),

    # Território
    "niv_terr": fields.String(attribute="territorio.nivel_territorial"),
    "cod_terr": fields.String(attribute="territorio.codigo_territorio"),
    "nom_terr": fields.String(attribute="territorio.nome_territorio"),

    # Classe Galináceos
    "cl_gal": fields.String(attribute="classe_galinaceos.codigo"),
    "nom_cl_gal": fields.String(attribute="classe_galinaceos.descricao"),

    # Métricas
    "e_cria_gal": fields.Integer,
    "e_tem_gal": fields.Integer,
    "e_gal_vend": fields.Integer,
    "gal_total": fields.Integer,
    "gal_vend": fields.Integer,
    "v_gal_vend": fields.Float,
    "vtp_agro": fields.Float,
    "rect_agro": fields.Float,
    "n_trab_total": fields.Integer,
}