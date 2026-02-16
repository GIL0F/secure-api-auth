from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
import re


class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str = "user"  # Campo de cargo (padrão 'user')

class UserCreate(UserBase):
    password: str


    @field_validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('A senha deve ter pelo menos 8 caracteres')
        if not re.search(r'[A-Z]', v):
            raise ValueError('A senha deve ter pelo menos uma letra maiúscula')
        if not re.search(r'[0-9]', v):
            raise ValueError('A senha deve ter pelo menos um número')
        return v

class UserResponse(UserBase):
    id: int
    

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None