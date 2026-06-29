from app.helpers.database import db

class Territorio(db.Model):
    __tablename__ = "territorio"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nivel_territorial = db.Column(db.String(10), nullable=False)
    codigo_territorio = db.Column(db.String(10), nullable=True)
    nome_territorio = db.Column(db.String(100), nullable=False)

    galinaceos = db.relationship("Galinaceos", back_populates="territorio")