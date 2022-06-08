from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

SQLALCHEMY_DATABASE_URI = "postgresql://user_local:12341234@localhost:5432/short_url"

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()