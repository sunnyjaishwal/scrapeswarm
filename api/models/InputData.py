import json
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

    def to_dict(self):
        return {
            "currency": self.currency,
            "sourceIata": self.sourceIata,
            "destinationIata": self.destinationIata,
            "departureDate": self.departureDate,
            "returnDate": self.returnDate,
            "pos": self.pos,
            "numOfAdults": self.numOfAdults,
            "numOfStops": self.numOfStops,
            "isRoundtrip": self.isRoundtrip
        }

class InputData(BaseModel):
    requestId: str
    reportId: str
    customerId: int
    # siteId: int
    # siteName: str
    retryCount: int
    parameters: Parameters

    def to_dict(self):
        return {
            "requestId": self.requestId,
            "reportId": self.reportId,
            "customerId": self.customerId,
            # "siteId": self.siteId,
            # "siteName": self.siteName,
            "retryCount": self.retryCount,
            "parameters": self.parameters.dict()
        }
