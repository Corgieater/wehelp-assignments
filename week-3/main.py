import urllib.request
import json
import csv
import re

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with urllib.request.urlopen(url) as response:
    data = json.load(response)  # turn response to json
    with open("data.csv", "w", encoding='utf-8', newline='') as file:  # encoding for traditional Chinese
        main_data = data["result"]["results"]
        main_data_length = len(main_data)
        writer = csv.writer(file, quoting=csv.QUOTE_NONE)

        for i in range(main_data_length):
            li = []
            stitle = main_data[i]['stitle']
            li.append(stitle)
            dist = main_data[i]["address"][5:8]
            li.append(dist)
            longitude = main_data[i]["longitude"]
            li.append(longitude)
            latitude = main_data[i]["latitude"]
            li.append(latitude)
            photos = main_data[i]["file"]
            photo = re.split(".jpg", photos, flags=re.IGNORECASE)
            li.append(photo[0]+'.jpg')
            writer.writerow(li)  # writerow expect an iterable object
