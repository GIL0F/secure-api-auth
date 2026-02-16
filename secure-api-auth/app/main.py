from fastapi import FastAPI
from app.db.database import engine
from app.users import models, routes 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes.router)  

@app.get("/")
def read_root():
    return {"message": "Servidor rodando!"}