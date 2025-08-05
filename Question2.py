""" 2. API Integration
 You have to build a Python script that pulls weather data from an API and stores only temperature
 and humidity in a CSV file every hour.
 Task: Describe how you'd structure this program using `requests`, `time.sleep`, and `csv`.
 """

import requests,time,csv
import pandas as pd

data_url=""
while True:
    response = requests.get(data_url)
    data = response.json()
    temp = data['temp']
    humidity = data['humidity']
    with open('weather.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([temp, humidity])