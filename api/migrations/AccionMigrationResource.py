import os
import aiofiles
import csv
from falcon import HTTPInternalServerError

from database import get_db_connection
from services.MigrationService import MigrationService


class AccionMigrationResource:
    service = MigrationService()

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
                    headers = ["col1", "col2", "col3", "col4"]
                    await self.service.build(content=content, batch_size=1000, table_name=table_name, headers=headers,
                                             conn=conn)

            except Exception as e:
                raise e
