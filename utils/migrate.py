import os
import aiofiles

from database import get_db_connection


class CommentsUtil:
    async def migrate(self):
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

                    await self.service.build(content=content, batch_size=500000, table_name=table_name, headers=headers,
                                             conn=conn)
            except Exception as e:
                raise e


# executing migrations

comments = CommentsUtil()
comments.migrate()
