from typing import List
from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from helpers.database import db


class Avicultor(db.Model):
    __tablename__ = "tb_avicultor"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String())
    nascimento: Mapped[datetime] = mapped_column(DateTime)
    cpf: Mapped[str] = mapped_column(String(11))
    caf: Mapped[str] = mapped_column(String())

    enderecos: Mapped[List["Endereco"]] = relationship(
        back_populates="avicultor",
        cascade="all, delete-orphan"
    )