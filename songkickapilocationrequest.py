
import requests
import json 

# r = requests.get('https://api.songkick.com/api/3.0/search/locations.json?query=Brooklyn&apikey=m9DM1BFnj2MsPG3R'): requesting info for nyc metropolitan area 
r = requests.get('https://api.songkick.com/api/3.0/metro_areas/7644/calendar.json?apikey=m9DM1BFnj2MsPG3R')
#above is requesting info for nyc metropolitan area 

print(r.status_code)

print(r.text)

data = json.loads(r.text)

print(data)







#requesting artist history:
 # https://api.songkick.com/api/3.0/artists/{artist_id}/gigography.json?apikey={m9DM1BFnj2MsPG3R}