from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.jwt import create_access_token, create_refresh_token
from jose import jwt, JWTError
from app.auth.jwt import SECRET_KEY, ALGORITHM
from pydantic import BaseModel
from app.auth.blacklist import add_token_to_blacklist
from app.auth.dependencies import oauth2_scheme

class RefreshTokenRequest(BaseModel):
    refresh_token: str

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != "admin" or form_data.password != "admin123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(data={"sub": form_data.username})
    refresh_token = create_refresh_token(data={"sub": form_data.username})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh_test")
def refresh_token(data: RefreshTokenRequest):
    try:
        payload = jwt.decode(
            data.refresh_token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")

        username = payload.get("sub")

        new_access_token = create_access_token(
            data={"sub": username}
        )

        return {"access_token": new_access_token, "token_type": "bearer"}

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired refresh token"
        )

@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    add_token_to_blacklist(token)
    return {"message": "Successfully logged out"}
