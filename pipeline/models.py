from config import DBURL

import enum
import sqlalchemy as sa
from sqlalchemy import Integer, String, ForeignKey, Float, Enum
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    # in case we want to add helper methods
    pass


class AggregationLevelEnum(enum.Enum):
    regional = 1
    national = 2


class RegionalMetrics(Base):
    __tablename__ = "regional_facts"

    # pk
    country_code: Mapped[String] = mapped_column(String, primary_key=True)
    region: Mapped[String] = mapped_column(String, primary_key=True)
    year: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    quarter: Mapped[Integer] = mapped_column(Integer, primary_key=True, nullable=True)
    level = mapped_column(Enum(AggregationLevelEnum))

    # Example mean column.
    cereal_yield = mapped_column(Float)
    # .... many other columns


def get_engine():
    return sa.create_engine(f"sqlite:////{DBURL}")


def create_db():
    engine = get_engine()
    Base.metadata.create_all(engine)  # should be Alembic up / downs

if __name__ == "__main__":
    create_db()
    print("created")
