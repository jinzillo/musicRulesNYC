# Mapping Music in NYC
 
Streaming services started to flourish around 2015 and have since become the primary way people listen to music. We initially created this project to explore what streaming services were trending on a national level compared to what artists were performing live in New York City. 

Our primary data sources came through Spotify, songkick, lastFM, and eventful. We used API’s to pull the data and python to parse through combinations of parameters then wrote the files to CSV.  We were able to pull longitude and latitude through the API to geocode our map. 

# Songkick/Last FM Script: Process and Instructions

I started with the songkick API. The API has different parameters you can focus on, but I chose to focus on location. In my script, I started by importing the “requests” and “json” modules, so that my results would come out in Json format. 
I set the metro area in the API endpoint to 7644, the code for the New York City metropolitan area, and made the api endpoint a string. The last part of the endpoint asks for your API key, which I also included. With this info added to the api endpoint, i created a response object “r” to store the results of my API “get” request. 

r = requests.get('https://api.songkick.com/api/3.0/metro_areas/7644/calendar.json?apikey=m9DM1BFnj2MsPG3R')

I then made sure to include a line checking the status code of my request using the “print” function, to make sure it was successful: print(r.status_code), and then wrote a print function to get the text of my request: print(r.text)

I then created a “data” variable: data = json.loads(r.text). The loads function helps parse the results of “r.text” into a json format. 

I finally ran the script using print(data), giving me all of the concerts in the New York City metropolitan area on November 15th, in a neat json format (sarah_data.json)

I then used openrefine to quickly convert the json results to a csv file that I could easily loop through, and named it “songkickresult.csv”

Next, I wanted to get the top tracks of each artist listed in the results i got from the songkick api request using the lastfm api endpoint. First I had to open the songkick results csv. 
For this script, I started by importing the necessary modules: csv, requests, json, and xml. This file is titled "artistsandvenuesloop.py."
I then used the ‘open’ function to open the csv file, and passed the results of this function to the variable ‘f’
To pull data from the CSV, I used the reader function to generate a reader object, which i set as “csv-f”
I then decided to do a for loop in order to pull the names of the artists from the csv. I set artist as a variable and indicated the position artist occupied on the csv (column 14)
I then inserted the last fm endpoint into my script, specifically requesting the top track of  specified artist. 
In order to pull the top tracks of each artist on the csv, i used string concatenation (inserting the artist variable into the api endpoint string using 2 plus signs) to pass the set ‘artist’ variable to the lastfm api, specifically the section where you set the artist parameter = to whichever artist you are requesting data on. 
I then ran the script and got the top tracks for each artist on the csv in xml format.  I pasted the results to a new file titled "finalartistandeventscript.xml." 

In order to run the script for "artistssandvenuesloop.py use python3 in the mac terminal and paste "artistsandvenuesloop.py" in the terminal. 
 

# Instructions for running eventful script:

•	The script available in rock_eventsListAPI.py loops through all events throught the eventful API. Various parameters such as date and query can be changed/updated to produce desired results. This code produces a json file that is then used to create CSV files using script rockEvents_allNov_csv.py which can also have various parameters (row 4). The code is commented to explain. For reference all CSVs that we produced with this code are also available in this repository.
Eventful API scripts need to be run in python 2.7.


 
