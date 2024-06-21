import os
import aiofiles
import csv
from falcon import HTTPInternalServerError

from database import get_db_connection


class CommentMigrationResource:

    async def on_post(self, req, resp):
        table_name = "comentarios"
        csv_file = os.path.join("resources", "testcomentarios.csv")
        try:
            await self.upload_csv_to_db(table_name, csv_file)
            resp.body = "file testcomentarios.csv was imported to table {}".format(table_name)
        except Exception as e:
            raise HTTPInternalServerError(description=str(e))

    async def upload_csv_to_db(self, table_name, csv_file):
        conn = await get_db_connection()

        async with conn.transaction():
            try:
                async with aiofiles.open(csv_file, mode='r', encoding="utf-8-sig") as file:
                    content = await file.read()
                    content_with_boom = content.lstrip('\ufeff')
                    rows = content_with_boom.splitlines()

                    reader = csv.reader(rows, delimiter='|')
                    batch_size = 500000
                    batch = []
                    headers = []
                    for i in range(0, 9):
                        headers.append(f"columna{i+1}")

                    placeholders = ', '.join(['$' + str(i + 1) for i in range(len(headers))])
                    insert_query = f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES ({placeholders})'
                    for row in reader:
                        if len(row) == 9:
                            batch.append(row)

                        if len(batch) >= batch_size:
                            await conn.executemany(insert_query, batch)
                            print("batch executing {} rows.".format(str(len(batch))))
                            batch = []
                    if batch:
                        await conn.executemany(insert_query, batch)


            except Exception as e:
                raise e
