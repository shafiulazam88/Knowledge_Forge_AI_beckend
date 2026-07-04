
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.modules.users.schema import UserResponse , UserRegister
from app.modules.users.service import UserService
from app.modules.users.repository import UserRepository
router = APIRouter(prefix="/auth", tags=["Authentication"])

def get_user_service(
        db: AsyncSession = Depends(get_db)
    )->UserService:
     repository = UserRepository(db)
     return UserService(repository)

@router.post("/register"
             ,
             response_model=UserResponse,

             status_code=201)
async def register(
     data: UserRegister,
     service: UserService = Depends(get_user_service)
    ):
     user = await service.register(data)
     return UserResponse.model_validate(user)
     