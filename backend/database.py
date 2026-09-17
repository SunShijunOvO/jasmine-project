from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from backend.config import settings
from sqlalchemy.engine import URL

db_url = URL.create(
    drivername="postgresql+psycopg",
    username=settings.user,
    password=settings.password.get_secret_value(),
    host=settings.host,
    port=settings.port,
    database=settings.name,
)

engine = create_engine(db_url)


class Base(DeclarativeBase):
    pass
