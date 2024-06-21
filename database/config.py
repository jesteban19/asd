import os

import asyncpg
from dotenv import load_dotenv


async def get_db_connection():
    load_dotenv()

    conn = await asyncpg.connect(
        user=os.getenv("USER"),
        password=os.getenv("PWD"),
        host="localhost",
        database=os.getenv("DATABASE")
    )
    return conn

async def get_db_session():
    return await get_db_connection()