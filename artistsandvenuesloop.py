
#looping through the results i got from the songkick api to get artist, venue, and date. 

import csv
import requests
import json
import xml


f = open('songkickresult.csv')

csv_f = csv.reader(f)


for row in csv_f:
	artist = row[14]
	r = requests.get('http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist='+artist+'&api_key=3dd81a709b61de2b8acc0c3a6fb0e991&') 
	# venue = row[28]
	# date = row[23]


	print(r.text, artist)

	# with open('bestartistscript.xml', 'w') as file: 
	# 	file.write(r.text)







  




