from app.helpers.database import db

class SistemaCriacao(db.Model):
    __tablename__ = "sistema_criacao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(db.String(20), nullable=False, unique=True)
    descricao = db.Column(db.String(100), nullable=False)

    galinaceos = db.relationship("Galinaceos", back_populates="sistema_criacao")