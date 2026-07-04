
from app.modules.users.schema import UserRegister, UserResponse
from app.modules.users.repository import UserRepository
from app.core.secuirity import hash_password
from app.modules.users.model import User

# the flow data will come from client then validate it using pydantic schema then pass it to service layer for business logic
#  then pass it to repository layer for database operations 
# then return the response to client
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    async def register(
            self,
            data: UserRegister
    )->User:
        existing_user = await self.repository.get_by_email(data.email)
        if existing_user:
            raise ValueError("User with this email already exists")
        
        user = User(
            email=data.email,
            password_hash=hash_password(data.password),
            full_name=data.full_name
        )

        return await self.repository.create(user)
        