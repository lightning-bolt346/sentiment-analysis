from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sentiments.db"

_engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)

def get_engine():
    return _engine

def get_session_maker():
    return _SessionLocal