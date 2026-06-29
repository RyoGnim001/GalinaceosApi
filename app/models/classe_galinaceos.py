from app.helpers.database import db

class ClasseGalinaceos(db.Model):
    __tablename__ = "classe_galinaceos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.Integer, nullable=False, unique=True)
    descricao = db.Column(db.String(100), nullable=False)

    galinaceos = db.relationship("Galinaceos", back_populates="classe_galinaceos")