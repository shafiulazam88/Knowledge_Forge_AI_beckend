from sqlalchemy import  String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.models.base_model import BaseModel

from app.db.base import Base

class User(Base, BaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
     )

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
     )

    role: Mapped[str] = mapped_column(
        String(50),
        default="user",
        nullable=False,
     )