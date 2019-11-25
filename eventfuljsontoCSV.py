import json

import csv

with open('events.json', 'r') as json_file:
    events_whole = json.load(json_file)

with open('eventfulEvents.csv',"w") as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(['show', 'club', 'latitude', 'longitude']) #sets up the writer header
    
    for event in events_whole: #extract specific data from each event
        show = event["title"]
        club = event["venue_name"]
        latitude = event['latitude']
        longitude = event['longitude']
        csv_writer.writerow([show, club, latitude, longitude])

print("done")

json_file.close()
csv_file.close()