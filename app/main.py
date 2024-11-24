from fastapi import FastAPI
import app.model as model
from app.config import engine
import app.router as router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def Home():
    return "Welcome Home"

app.include_router(router.router, prefix='/wandr', tags=['wandr'])
