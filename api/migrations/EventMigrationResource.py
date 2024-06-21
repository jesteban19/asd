import os
import aiofiles
import csv
from falcon import HTTPInternalServerError

from database import get_db_connection
from services.MigrationService import MigrationService


class EventMigrationResource:
    service = MigrationService()

    async def on_post(self, req, resp):
        table_name = "eventos"
        csv_file = os.path.join("resources", "testevento.csv")
        try:
            await self.upload_csv_to_db(table_name, csv_file)
            resp.body = "file testevento.csv was imported to table {}".format(table_name)
        except Exception as e:
            raise HTTPInternalServerError(description=str(e))

    async def upload_csv_to_db(self, table_name, csv_file):
        conn = await get_db_connection()

        async with conn.transaction():
            try:
                async with aiofiles.open(csv_file, mode='r', encoding="utf-8-sig") as file:
                    content = await file.read()
                    headers = []
                    for i in range(0, 27):
                        headers.append(f"columna{i + 1}")

                    await self.service.build(content=content, batch_size=500000, table_name=table_name, headers=headers,
                                             conn=conn)
            except Exception as e:
                raise e
