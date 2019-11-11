import requests
import json 


r = requests.get('https://api.songkick.com/api/3.0/artists/73965093/similar_artists.json?apikey=m9DM1BFnj2MsPG3R')
#r = requests.get('https://api.songkick.com/api/3.0/metro_areas/7644/calendar.json?apikey=m9DM1BFnj2MsPG3R')
#above is requesting info about artists and their shows in an area


print(r.status_code)

print(r.text)

data = json.loads(r.text)

print(data)

