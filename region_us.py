import csv

with open('globalRegion_Spotify.csv') as csv_input:

	with open('us_Spotify.csv',"w") as us_Results:

		csv_results = csv.reader(csv_input)

		csv_writer = csv.writer(us_Results) #sets up the writer



		for row in csv_results:

			# us_data = row [0,1,2]
			
			position = row[0]
			trackname = row[1]
			artist = row[2]
			streams = row[3]
			URL = row[4]
			Date = row[5]
			country = row [6]

			if country == 'us':

				csv_writer.writerow(row)

				# print(position, trackname, artist)