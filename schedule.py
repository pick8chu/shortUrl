from routes.shorturl.controllers import deleteOldShortLinks
from fastapi_utils.tasks import repeat_every
from database import SQLALCHEMY_DATABASE_URI
from fastapi_utils.session import FastAPISessionMaker

sessionmaker = FastAPISessionMaker(SQLALCHEMY_DATABASE_URI)

# db 하루에 한번씩 배치 돌면서 없애기. -> 마지막 조회일자 기준
@repeat_every(seconds=60 * 60 * 24)    # 1 day
def scheduledAddQuoteList():
    print("executed :: deleteOldShortLinks")
    with sessionmaker.context_session() as db:
        minuteOld = 60 * 24 * 30    # 1 month old
        deleteOldShortLinks(minuteOld, db)
