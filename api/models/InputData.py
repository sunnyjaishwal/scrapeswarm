from pydantic import BaseModel

class InputData(BaseModel):
    siteId : int
    siteName : str
    siteUrl : str
    siteDescription : str
    sourceIATA : str
    destinationIATA : str
    departureDate : str
    requestId : str
    requestTime : str
    sourceIP : str