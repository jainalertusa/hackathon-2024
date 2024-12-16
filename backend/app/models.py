from sqlalchemy import Column, Integer, String, Float, Text
from .database import Base

class Property(Base):
    __tablename__ = "Properties"
    id = Column(String, primary_key=True, index=True)
    pin = Column(String, index=True)
    houseType = Column(String)
    address = Column(String)
    price = Column(Float)
    beds = Column(Integer)
    baths = Column(Integer)
    sqft = Column(Float)
    parking = Column(Integer)
    construction = Column(Integer)
    pricePerSqft = Column(Float)
    homeOwnersAssociationFees = Column(Float)
    tax = Column(Float)
    taxYear = Column(Integer)
    imgUrls = Column(String)

class Features(Base):
    __tablename__ = "Features"
    id = Column(String, primary_key=True, index=True)
    safety = Column(Float)
    schoolCount = Column(Integer)
    sideWalkScore = Column(Integer)
    transitScore = Column(Integer)
    weatherScore = Column(Integer)
    weatherRisks = Column(Text) 

