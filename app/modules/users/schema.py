# only validation pydantic schema
from pydantic import BaseModel , ConfigDict , EmailStr , Field
from uuid import UUID
class UserRegister(BaseModel):
     email : EmailStr
     password : str = Field(min_length=8, max_length=128)
     full_name: str = Field(min_length=2, max_length=100)

class UserResponse(BaseModel):
     id: UUID
     email: EmailStr
     full_name: str
     role : str
     model_config=ConfigDict(from_attributes=True)