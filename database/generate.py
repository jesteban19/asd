from database.config import engine, Base

Base.metadata.create_all(engine)
