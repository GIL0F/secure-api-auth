from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get("sub")

@router.get("/me")
def read_users_me(current_user: str = Depends(get_current_user)):
    return {"user": current_user}
