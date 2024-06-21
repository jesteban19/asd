import csv
import io

from database import get_db_connection
from database.orm import get_session_orm
from schemas.models import CommentModel


class CommentService:
    async def upload(self, file_content):
        session = await get_session_orm()

        file_str = file_content.decode('utf-8')
        file = io.StringIO(file_str)
        rows = csv.reader(file, delimiter='|')
        batch_size = 2000
        batch = []
        for row in rows:
            batch.append(CommentModel(
                columna1=row[0],
                columna2=row[1],
                columna3=row[2],
                columna4=row[3],
                columna5=row[4],
                columna6=row[5],
                columna7=row[6],
                columna8=row[7],
                columna9=row[8],
            ))
            if len(batch) >= batch_size:
                try:
                    session.bulk_save_objects(batch)
                    session.commit()
                    batch.clear()
                except Exception as e:
                    raise e
                finally:
                    session.close()

        if batch:
            try:
                session.bulk_save_objects(batch)
                session.commit()
                batch.clear()
            except Exception as e:
                raise e
            finally:
                session.close()
