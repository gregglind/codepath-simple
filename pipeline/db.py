import sqlalchemy


def create_db():
    engine = create_engine("sqlite://")
    Modelbase.metadata.create_all(engine)  # should be Alembic up / downs
