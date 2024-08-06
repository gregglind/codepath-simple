from config import DBURL

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


def create_db():
    engine = create_engine(f"sqlite:////{DBURL}")
    # Modelbase.metadata.create_all(engine)  # should be Alembic up / downs
