from fastapi import APIRouter
from app.auth.jwt import create_access_token
from app.users.models import User

router = APIRouter()

@router.post("/login")
def login(user: User):
    # Simples (mock) — depois vai virar banco + hash
    if user.username == "admin" and user.password == "admin":
        token = create_access_token({"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    
    return {"error": "invalid credentials"}
