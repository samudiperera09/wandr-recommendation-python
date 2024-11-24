from sqlalchemy.orm import Session
from app.model import Traveller, Category, Activities
from app.schemas import TravellerSchema, ActivitySchema, CategorySchema

def get_traveller(db:Session,skip:int=0,limit:int=100):
    return db.query(Traveller).offset(skip).limit(limit).all()

def get_traveller_by_id(db: Session, traveller_id: int):
    return db.query(Traveller).filter(Traveller.traveller_id == traveller_id).first()
#     if traveller:
#         category_ids = traveller.category_ids
#         activity_ids = traveller.activity_ids

#         categories = db.query(Category).filter(Category.category_id.in_(category_ids)).all() if category_ids else []
#         activities = db.query(Activities).filter(Activities.activity_id.in_(activity_ids)).all() if activity_ids else []

#         category_schemas = [CategorySchema.from_orm(category) for category in categories]
#         activity_schemas = [ActivitySchema.from_orm(activity) for activity in activities]

#         return TravellerSchema(
#             id=traveller.traveller_id,
#             name=traveller.name,
#             country=traveller.country,
#             categories=category_schemas,
#             activities=activity_schemas
#         )
#     return None