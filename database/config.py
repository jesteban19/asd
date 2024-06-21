import asyncpg

async def get_db_connection():
    conn = await asyncpg.connect(
        user="devttecnico22",
        password="Jyuwh%cwe=",
        host="localhost",
        database="devttecnico22"
    )
    return conn

async def get_db_session():
    return await get_db_connection()