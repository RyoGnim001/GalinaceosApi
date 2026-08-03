from sqlalchemy import String, Float, Integer,  ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.helpers.database import db


class Aviario(db.Model):
    __tablename__ = "tb_aviario"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidade: Mapped[int] = mapped_column(Integer, nullable=False)
    area: Mapped[float] = mapped_column(Float, nullable=False)

    avicula_id: Mapped[int] = mapped_column(
        ForeignKey("tb_avicula.id"),
        nullable=False
    )

    avicula: Mapped["Avicula"] = relationship(
        back_populates="aviarios"
    )