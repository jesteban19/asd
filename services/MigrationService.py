import csv


class MigrationService:

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
