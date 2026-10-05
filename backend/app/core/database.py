from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.models.base import Base
from app.core.config import settings


connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
pool_options = {} if settings.database_url.startswith("sqlite") else {"pool_size": settings.db_pool_size, "max_overflow": settings.db_max_overflow, "pool_timeout": settings.db_pool_timeout, "pool_pre_ping": True}
engine = create_engine(settings.database_url, connect_args=connect_args, future=True, **pool_options)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
