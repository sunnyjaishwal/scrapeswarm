from pydantic import BaseModel, Field # type: ignore
from typing import Dict

from pydantic import BaseModel # type: ignore

class Parameters(BaseModel):
    currency: str
    sourceIata: str
    destinationIata: str
    departureDate: str
    returnDate: str
    pos: str
    numOfAdults: int
    numOfStops: int
    isRoundtrip: bool

class InputData(BaseModel):
    requestId: str
    reportId: str
    customerId: int
    siteId: int
    siteName: str
    retryCount: int
    parameters: Parameters
