import csv
import os
import aiofiles
import asyncpg
import asyncio

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


class MigrateTools:
    async def migrate_comments(self):
        table_name = "comentarios"
        csv_file = os.path.join("resources", "testcomentarios.csv")
        await self.upload_csv_to_db(table_name, csv_file)

    async def upload_csv_to_db(self, table_name, csv_file):
        conn = await get_db_connection()

        async with conn.transaction():
            try:
                async with aiofiles.open(csv_file, mode='r', encoding="utf-8-sig") as file:
                    content = await file.read()
                    headers = []
                    for i in range(0, 9):
                        headers.append(f"columna{i + 1}")

                    await self.build(content=content, batch_size=500000, table_name=table_name, headers=headers,
                                     conn=conn)
            except Exception as e:
                raise e

    async def build(self, content, batch_size, table_name, headers, conn):
        content_with_boom = content.lstrip('\ufeff')
        rows = content_with_boom.splitlines()
        reader = csv.reader(rows, delimiter='|')
        batch = []
        placeholders = ', '.join(['$' + str(i + 1) for i in range(len(headers))])
        insert_query = f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES ({placeholders})'
        for row in reader:
            if len(row) == len(headers):
                batch.append(row)
            if len(batch) >= batch_size:
                await conn.executemany(insert_query, batch)
                batch = []
        if batch:
            await conn.executemany(insert_query, batch)


# executing migrations

async def runAll():
    try:
        comments = MigrateTools()
        await comments.migrate_comments()
    except Exception as e:
        raise e

asyncio.run(runAll())