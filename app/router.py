from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import TravellerSchema,RequestTraveller,Response,Request
import crud 

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/')
async def get_traveller(db:Session = Depends(get_db)):
    _traveller = crud.get_traveller(db,0,100)
    return Response(code = "200", status = 'ok', message = "Success Fetch All Data", result=_traveller).dict(exclude_none = True)

@router.get('/{id}')
async def get_by_id(id:int, db:Session = Depends(get_db)):
    _traveller = crud.get_traveller_by_id(db,id)
    return Response(code = "200", status = 'ok', message = "Success get Data", result = _traveller).dict(exclude_none = True)