from app.helpers.database import db

class Galinaceos(db.Model):
    __tablename__ = "galinaceos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sist_cria_id = db.Column(db.Integer, db.ForeignKey("sistema_criacao.id"), nullable=False)
    territorio_id = db.Column(db.Integer, db.ForeignKey("territorio.id"), nullable=False)
    cl_gal_id = db.Column(db.Integer, db.ForeignKey("classe_galinaceos.id"), nullable=False)

    e_cria_gal = db.Column(db.BigInteger, nullable=True)
    e_tem_gal = db.Column(db.BigInteger, nullable=True)
    e_gal_vend = db.Column(db.BigInteger, nullable=True)
    gal_total = db.Column(db.BigInteger, nullable=True)
    gal_vend = db.Column(db.BigInteger, nullable=True)
    v_gal_vend = db.Column(db.Numeric, nullable=True)
    vtp_agro = db.Column(db.Numeric, nullable=True)
    rect_agro = db.Column(db.Numeric, nullable=True)
    n_trab_total = db.Column(db.BigInteger, nullable=True)

    sistema_criacao = db.relationship("SistemaCriacao", back_populates="galinaceos")
    territorio = db.relationship("Territorio", back_populates="galinaceos")
    classe_galinaceos = db.relationship("ClasseGalinaceos", back_populates="galinaceos")