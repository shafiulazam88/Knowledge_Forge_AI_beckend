#base class for all models , every model will inherit from this class

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass