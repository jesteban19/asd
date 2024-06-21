import asyncpg

async def get_db_connection():
    conn = await asyncpg.connect(
        user="postgres",
        password="123",
        host="localhost",
        database="evolta"
    )
    return conn

async def get_db_session():
    return await get_db_connection()