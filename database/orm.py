import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

async def get_session_orm():
    load_dotenv()
    db_url = f'postgresql://{os.getenv("USER")}:{os.getenv("PASSWORD")}@127.0.0.1:5432/{os.getenv("DATABASE")}'
    print(db_url)
    engine = create_engine(db_url)
    session = sessionmaker(bind=engine)
    return session()
