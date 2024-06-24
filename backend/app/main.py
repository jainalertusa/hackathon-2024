from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
from .database import SessionLocal, engine
from .models import Base, Property, Features
from .utils import generate_pdf
from . import schemas 

# APIRouter import to create routers
from fastapi import APIRouter

# An instance of APIRouter created
router = APIRouter()

Base.metadata.create_all(bind=engine)

# Function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint definition using router
# Endpoint to fetch all the properties for a particular zipcode.
@router.get("/apartments/{pin}", response_model=List[schemas.Property])
async def get_properties_by_pin(pin: str, db: Session = Depends(get_db)):
    print("here")
    properties = db.query(Property).filter(Property.pin == pin).all()
    if not properties:
        raise HTTPException(status_code=404, detail="Properties not found for the given zipcode")
    return properties

# Endpoint to fetch all the property detaisl for a particular apartment id.
@router.get("/apartment/{apartment_id}", response_model=schemas.Property)
async def get_property(apartment_id: str, db: Session = Depends(get_db)):
    property = db.query(Property).filter(Property.id == apartment_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

# Endpoint to download the property analysis pdf report.
@router.get("/apartment/{apartment_id}/pdf")
async def get_property_pdf(apartment_id: str, db: Session = Depends(get_db)):
    property = db.query(Property).filter(Property.id == apartment_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    features = db.query(Features).filter(Features.id == apartment_id).first()
    # print("here")
    # print(schemas.Features.fire)
    if not features:
        raise HTTPException(status_code=404, detail="Analysis parameters not found!")

    features_schema = schemas.Features(
        id=features.id,
        safety=features.safety,
        schoolCount=features.schoolCount,
        sideWalkScore=features.sideWalkScore,
        transitScore=features.transitScore,
        weatherScore=features.weatherScore,
        weatherRisks=features.weatherRisks
    )

    pdf_file = generate_pdf(property, features_schema)
    return FileResponse(pdf_file, media_type='application/pdf', filename=f"{property.id}.pdf")


# Create an instance of FastAPI
app = FastAPI()

# Include the router instance in the app
app.include_router(router, prefix="/api")  # You can change the prefix as needed
