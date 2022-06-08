from fastapi import FastAPI, Depends, Request, Response, Query, Body
from routes.shorturl.router import router
from fastapi.middleware.cors import CORSMiddleware
import schedule 
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# logger.addHandler(logHandler)

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["http://localhost:8080", "Access-Control-Allow-Origin"],
)

# schedule job
@app.on_event("startup")
async def scheduledAddQuoteList():
    await schedule.scheduledAddQuoteList()