import json
from pydantic import BaseModel, Field # type: ignore
from typing import Dict

from pydantic import BaseModel


class URLRequest(BaseModel):
    url: str