import os
import aiofiles
import csv
from falcon import HTTPInternalServerError

from database import get_db_connection


class AccionMigrationResource:

    async def on_post(self, req, resp):
        table_name = "accion"
        csv_file = os.path.join("resources", "testaccion.csv")
        try:
            await self.upload_csv_to_db(table_name, csv_file)
            resp.body = "file testaccion.csv was imported to table {}".format(table_name)
        except Exception as e:
            raise HTTPInternalServerError(description=str(e))

    async def upload_csv_to_db(self, table_name, csv_file):
        conn = await get_db_connection()

        async with conn.transaction():
            try:
                async with aiofiles.open(csv_file, mode='r', encoding="utf-8") as file:
                    content = await file.read()
                    rows = content.splitlines()

                    reader = csv.reader(rows, delimiter='|')
                    batch_size = 1000
                    batch = []
                    headers = ["col1", "col2", "col3", "col4"]
                    placeholders = ', '.join(['$' + str(i + 1) for i in range(len(headers))])
                    insert_query = f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES ({placeholders})'
                    for row in reader:
                        row[0] = int(row[0])
                        batch.append(row)
                        if len(batch) >= batch_size:
                            await conn.executemany(insert_query, batch)
                            batch = []
                    if batch:
                        await conn.executemany(insert_query, batch)


            except Exception as e:
                await conn.rollback()
                raise e
