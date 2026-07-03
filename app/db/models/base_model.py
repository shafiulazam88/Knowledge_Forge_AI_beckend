#reusable base model for all models to inherit from

from datetime import datetime
from uuid import uuid4, UUID

from sqlalchemy import  DateTime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID

class BaseModel:
     id:Mapped[UUID] =mapped_column(
          PGUUID(as_uuid=True),
            primary_key=True, default=uuid4, 
            unique=True,
            index=True
     )
     created_at:Mapped[datetime] =mapped_column(
          
          DateTime(timezone=True), 
          server_default=func.now(),
     )

     updated_at:Mapped[datetime] =mapped_column(
          DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
     )
