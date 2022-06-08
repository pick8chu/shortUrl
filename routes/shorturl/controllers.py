from sqlalchemy.orm import Session
from models import Url
from sqlalchemy import and_, or_, not_
from .schemas import BaseUrl, ShortUrl
from pytz import timezone
from fastapi import HTTPException, Query
from datetime import datetime, timedelta
import random

charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def addShortLink(baseUrl:BaseUrl, db:Session):
    reqUrl = baseUrl.url.strip()
    if reqUrl[:7] != "http://" and reqUrl[:8] != "https://":
        raise HTTPException(status_code=400, detail=f"url is not valid: {baseUrl.url}")    
    
    shortId=generateShortId(db)
    curDtm = datetime.now(timezone('Asia/Seoul'))
    url = Url(id=shortId, url=reqUrl.strip(), create_dtm=curDtm, last_used_dtm=curDtm)
    db.add(url)
    db.commit()
    return url.toShortUrl()
    

def getShortLink(shortId:str, db:Session):
    res = db.query(Url).filter(Url.id == shortId).one_or_none()
    if res is None:
        raise HTTPException(status_code=404, detail=f"No match found for short_id: {shortId}")
    res.last_used_dtm = datetime.now(timezone('Asia/Seoul'))
    db.commit()
    return res.toShortUrl()
    
def redirect(shortId:str, db:Session):
    return getShortLink(shortId, db).url


def generateShortId(db:Session) -> str:
    shortId = getBase62()
    idList = list(map(lambda url: url.id, db.query(Url).all()))
    while shortId in idList:
        shortId = getBase62()
    return shortId

def getBase62() -> str:
    return "".join([charset[random.randrange(0,62)] for i in range(5)])

def deleteOldShortLinks(minuteOld:int, db:Session) -> str:
    nthMinuteAgo = datetime.now(timezone('Asia/Seoul')) - timedelta(minutes=minuteOld)
    db.query(Url).filter(Url.last_used_dtm <= nthMinuteAgo).delete()
    db.commit()