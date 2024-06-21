from database import get_db_connection


async def select_last_comment_by_id(id):
    conn = await get_db_connection()
    async with conn.transaction():
        try:
            return await conn.fetch(
                "select * from comentarios where columna4='{}' order by TO_DATE(columna7,'YYYY-MM-DD H:m:s') desc limit 1".format(
                    id))
        except Exception as e:
            raise e


async def get_actions_by_id(id):
    conn = await get_db_connection()
    async with conn.transaction():
        try:
            return await conn.fetch(
                "select * from comentarios where columna4='{}' order by TO_DATE(columna7,'YYYY-MM-DD H:m:s') desc limit 1".format(
                    id))
        except Exception as e:
            raise e


async def get_recent_actions(id):
    conn = await get_db_connection()
    async with conn.transaction():
        try:
            return await conn.fetch(
                "select * from eventos where columna5='7' and columna23='{}' order by columna1 desc limit 5".format(id)
            )
        except Exception as e:
            raise e


async def insert_event(params):
    conn = await get_db_connection()
    async with conn.transaction():
        try:
            query = """
                INSERT INTO eventos (columna1, columna2, columna3, columna4, columna5, columna6,
                                         columna7, columna8, columna9, columna10, columna11, columna12,
                                         columna13, columna14, columna15, columna16, columna17, columna18,
                                         columna19, columna20, columna21, columna22, columna23, columna24, columna25, columna26, columna27)
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18,
                        $19, $20, $21, $22, $23, $24, $25, $26, $27)
            """
            await conn.execute(query, *params)
        except Exception as e:
            raise e


async def update_comment(id, comment):
    conn = await get_db_connection()
    async with conn.transaction():
        try:
            query = """
                update comentarios set columna5=$1 where columna4=$2 
            """
            await conn.execute(query, comment, id)
        except Exception as e:
            raise e

