from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ ="users"
    id:Mapped[int] = mapped_column(Integer ,primary_key = True )
    name:Mapped[str]= mapped_column(String(50) , nullable =False)
    email:Mapped[str]= mapped_column(String(50) , nullable =False, unique =True)



