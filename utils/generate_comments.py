import csv
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()
start_id = 800000
increment_id = 900000
unique_id_start = 347
timestamp_start = datetime(2016, 1, 10, 4, 14, 10, 183000)

num_records = 2500

with open(os.path.join("resources", "fake_data.csv"), mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='|')
    for i in range(num_records):
        record_id = start_id + i
        increment_record_id = increment_id + i
        unique_id = unique_id_start + i
        comment = fake.sentence()
        timestamp = timestamp_start + timedelta(seconds=i)
        writer.writerow([record_id, '', '', increment_record_id, comment, unique_id, timestamp.isoformat(), '', ''])

print("file csv 'resources/fake_data.csv' was created")
