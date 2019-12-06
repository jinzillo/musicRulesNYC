
import csv

with open('us_Spotify2.csv') as csv_input:

	with open('spotifyNovember17.csv',"w") as csv_Results:

		csv_results = csv.reader(csv_input)

		csv_writer = csv.writer(csv_Results) #sets up the writer



		for row in csv_results:

			# us_data = row [0,1,2]
			
			position = row[0]
			trackname = row[1]
			artist = row[2]
			streams = row[3]
			URL = row[4]
			date = row[5]
			country = row [6]

			if date == '11/15/17':

				csv_writer.writerow(row)

				# print(position, trackname, artist)