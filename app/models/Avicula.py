from typing import List

from sqlalchemy import String, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.helpers.database import db


class Avicula(db.Model):
    __tablename__ = "tb_avicula"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String())
    capacidade: Mapped[int] = mapped_column(Integer, nullable=False)
    area: Mapped[float] = mapped_column(Float)

    avicultor_id: Mapped[int] = mapped_column(
        ForeignKey("tb_avicultor.id")
    )

    aviarios: Mapped[List["Aviario"]] = relationship(
        back_populates="avicula",
        cascade="all, delete-orphan"
    )

    galpoes: Mapped[List["Galpao"]] = relationship(
        back_populates="avicula",
        cascade="all, delete-orphan"
    )