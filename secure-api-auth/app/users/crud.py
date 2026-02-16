from sqlalchemy.orm import Session
from . import models, schemas
# Agora importamos o nome CORRETO que definimos no passo 1
from .security import get_password_hash 

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    # Usando a função com o nome correto
    hashed_pw = get_password_hash(user.password)
    
    db_user = models.User(
        email=user.email, 
        username=user.username, 
        hashed_password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user