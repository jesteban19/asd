import csv
import io

from database import get_db_connection


class CommentService:
    async def upload(self, file_content):
        file_str = file_content.decode('utf-8')
        file = io.StringIO(file_str)
        rows = csv.reader(file, delimiter='|')
        batch_size = 2000
        batch = []
        headers = [f"columna{i + 1}" for i in range(9)]

        placeholders = ', '.join(['$' + str(i + 1) for i in range(len(headers))])
        insert_query = f'INSERT INTO comentarios ({", ".join(headers)}) VALUES ({placeholders})'

        conn = await get_db_connection()
        async with conn.transaction():
            for row in rows:
                batch.append(tuple(row))
                if len(batch) >= batch_size:
                    await conn.executemany(insert_query, batch)
                    batch.clear()

            if batch:
                await conn.executemany(insert_query, batch)
