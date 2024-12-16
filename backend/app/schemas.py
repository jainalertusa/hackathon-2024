from pydantic import BaseModel
from typing import Optional, List

class Property(BaseModel):
    id: str
    pin: str
    houseType: str
    address: str
    price: float
    beds: Optional[float] = None
    baths: Optional[float] = None
    sqft: Optional[float] = None
    parking: Optional[float] = None
    construction: Optional[int] = None
    pricePerSqft: Optional[float] = None
    homeOwnersAssociationFees: Optional[float] = None
    tax: Optional[float] = None
    taxYear: Optional[int] = None
    imgUrls: Optional[str] = None

class Features(BaseModel):
    id: str
    safety: float
    schoolCount: int
    sideWalkScore: int
    transitScore: int
    weatherScore: int
    weatherRisks: str 

    @property
    def flood(self) -> str:
        return self.weatherRisks.split(',')[0] if self.weatherRisks else ''

    @property
    def fire(self) -> str:
        return self.weatherRisks.split(',')[1] if self.weatherRisks and len(self.weatherRisks.split(',')) > 1 else ''

    @property
    def wind(self) -> str:
        return self.weatherRisks.split(',')[2] if self.weatherRisks and len(self.weatherRisks.split(',')) > 2 else ''

    @property
    def air(self) -> str:
        return self.weatherRisks.split(',')[3] if self.weatherRisks and len(self.weatherRisks.split(',')) > 3 else ''

    @property
    def heat(self) -> str:
        return self.weatherRisks.split(',')[4] if self.weatherRisks and len(self.weatherRisks.split(',')) > 4 else ''
    
    class Config:
        orm_mode = True
