from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str


class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
