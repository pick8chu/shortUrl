import datetime
from xmlrpc.client import DateTime
from pydantic import BaseModel
from typing import List, Optional

class BaseUrl(BaseModel):
    url: str

class ShortUrl(BaseModel):
    shortId: str
    url: str
    createAt: datetime.datetime
