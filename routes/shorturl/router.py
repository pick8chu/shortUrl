from csv import list_dialects
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from . import controllers
from database import get_db
from .schemas import BaseUrl, ShortUrl
from starlette.responses import RedirectResponse

router = APIRouter()

@router.post("/short-links")
def addShortLink(baseUrl: BaseUrl, db: Session = Depends(get_db)) -> ShortUrl:
    return controllers.addShortLink(baseUrl, db)
     
@router.get("/short-links/{shortId}")
def getShortLink(shortId: str, db: Session = Depends(get_db)) -> ShortUrl:
    return controllers.getShortLink(shortId, db)

@router.get("/{shortId}", response_class=RedirectResponse, status_code=302)
def redirect(shortId: str, db: Session = Depends(get_db)) -> ShortUrl:
    return controllers.redirect(shortId, db)
     
