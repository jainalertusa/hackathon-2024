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
        risks = self.weatherRisks.strip("[]").replace('"', '').replace("'", "").split(',')
        return risks[0].strip() if risks else ''

    @property
    def fire(self) -> str:
        risks = self.weatherRisks.strip("[]").replace('"', '').replace("'", "").split(',')
        return risks[1].strip() if len(risks) > 1 else ''

    @property
    def wind(self) -> str:
        risks = self.weatherRisks.strip("[]").replace('"', '').replace("'", "").split(',')
        return risks[2].strip() if len(risks) > 2 else ''

    @property
    def air(self) -> str:
        risks = self.weatherRisks.strip("[]").replace('"', '').replace("'", "").split(',')
        return risks[3].strip() if len(risks) > 3 else ''

    @property
    def heat(self) -> str:
        risks = self.weatherRisks.strip("[]").replace('"', '').replace("'", "").split(',')
        return risks[4].strip() if len(risks) > 4 else ''
    
    class Config:
        orm_mode = True
