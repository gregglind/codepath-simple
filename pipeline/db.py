import sqlalchemy

def create_db():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)  # should be Alembic up / downs
