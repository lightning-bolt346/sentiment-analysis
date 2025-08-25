try:
    from sqlalchemy.orm import declarative_base  # type: ignore
    Base = declarative_base()
except Exception:  # SQLAlchemy may not be installed yet
    Base = object  # type: ignore