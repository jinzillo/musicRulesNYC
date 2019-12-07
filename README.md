# Mapping Music in NYC
 
Streaming services started to flourish around 2015 and have since become the primary way people listen to music. We initially created this project to explore what streaming services were trending on a national level compared to what artists were performing live in New York City. 

Our primary data sources came through Spotify, songkick, lastFM, and eventful. We used API’s to pull the data and python to parse through combinations of parameters then wrote the files to CSV.  We were able to pull longitude and latitude through the API to geocode our map. 

# Instructions for running eventful script:

•	The script available in rock_eventsListAPI.py loops through all events throught the eventful API. The various parameters can be changed/updated to produce desired results. This code produces a json file that is then used to create a csv. The code is commented to explain.
Eventful API scripts need to be run in python 2.7.

•	The script in rockEvents_allNov_csv.py is used to produce the various csv files used for mapping. Json files can be swapped out in row 4 to produce various mappings.

•	For reference all CSVs that we produced with this code are also available in this repository. 
