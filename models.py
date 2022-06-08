from decimal import Decimal
from sqlalchemy import Column, ForeignKey, Integer, String, Float, BigInteger, DateTime, Date, Numeric, Boolean, Text, BigInteger, null # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from database import Base
from routes.shorturl.schemas import ShortUrl

class Url(Base):
    __tablename__ = "short_url_mt"

    id = Column(String(5), primary_key=True)
    url = Column(String(4000))
    last_used_dtm = Column(DateTime, server_default="now()")
    create_dtm = Column(DateTime, server_default="now()")

    def toShortUrl(self):
        return ShortUrl(shortId=self.id, url=self.url, createAt=self.create_dtm)
