from marshmallow import Schema, fields

class GalinaceosSchema(Schema):
    id = fields.Int()
    
    # Sistema de Criação
    sist_cria = fields.Method("get_sist_cria")
    
    # Território
    niv_terr = fields.Method("get_niv_terr")
    cod_terr = fields.Method("get_cod_terr")
    nom_terr = fields.Method("get_nom_terr")
    
    # Classe Galináceos
    cl_gal = fields.Method("get_cl_gal")
    nom_cl_gal = fields.Method("get_nom_cl_gal")
    
    # Métricas
    e_cria_gal = fields.Int()
    e_tem_gal = fields.Int()
    e_gal_vend = fields.Int()
    gal_total = fields.Int()
    gal_vend = fields.Int()
    v_gal_vend = fields.Float()
    vtp_agro = fields.Float()
    rect_agro = fields.Float()
    n_trab_total = fields.Int()

    def get_sist_cria(self, obj):
        return obj.sistema_criacao.codigo if obj.sistema_criacao else None

    def get_niv_terr(self, obj):
        return obj.territorio.nivel_territorial if obj.territorio else None

    def get_cod_terr(self, obj):
        return obj.territorio.codigo_territorio if obj.territorio else None

    def get_nom_terr(self, obj):
        return obj.territorio.nome_territorio if obj.territorio else None

    def get_cl_gal(self, obj):
        return obj.classe_galinaceos.codigo if obj.classe_galinaceos else None

    def get_nom_cl_gal(self, obj):
        return obj.classe_galinaceos.descricao if obj.classe_galinaceos else None