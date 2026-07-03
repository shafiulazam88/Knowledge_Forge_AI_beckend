#just pure database operations, no business logic, no validation, no serialization, no deserialization

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.users.model import User

class UserRepository:
    def __init__(self, db: AsyncSession):
         self.db = db
    async def get_bye_email(self, email:str)->User|None:
         query = select(User).where(User.email == email)
         result = await self.db.execute(query)
         return result.scalar_one_or_none()
    async def create(self , user:User)->User:
         self.db.add(user)
         await self.db.commit()
         await self.db.refresh(user)
         return user