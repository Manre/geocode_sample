"""
1. Create virtualenv, virtualenv -p python3 venv
2. Activate it:
  cd venv
  . bin/activate
  mkdir geothing
  cd geothing
3. export google api key:
  export GOOGLE_API_KEY=[my-key]
4. pip install -r requirements.txt
5. Create a file named data.csv just like this:
  Carrera 69 No 80-20 Bogotá, Colombia
  Carrera 7Bis No 106-33 Bogotá, Colombia
6. python init.py, I will create a file result.csv with the result :P
"""
from geocoder import google
import time
import csv

output_results = []
with open('data.csv', 'r', newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter='|')
  for row in reader:
    direction = row[0]

    if direction == 'direction':
        continue
    time.sleep(1)
    print(direction)
    result = google(direction)
    latitude = result.latlng[0]
    longitude = result.latlng[1]
    line = '{}|{}|{}'.format(
      direction,
      latitude,
      longitude,
    )
    output_results.append(line)


out_file = open('result.csv', 'w+')
for line in output_results:
    out_file.write(line + '\r\n')
out_file.close()
