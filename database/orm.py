import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

async def get_session_orm():
    load_dotenv()
    db_url = f'postgresql://{os.getenv("USER")}:{os.getenv("PWD")}@127.0.0.1:5432/{os.getenv("DATABASE")}'
    engine = create_engine(db_url)
    session = sessionmaker(bind=engine)
    return session()
