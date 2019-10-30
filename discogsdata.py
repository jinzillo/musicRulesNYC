import csv
import xml.etree.cElementTree as ET


tree = ET.parse('discogscondense.xml')
root = tree.getroot()

discogs_data = open('DiscogsCondense.csv', 'w')

discogs_head = []

csvwriter = csv.writer(discogs_data)


count = 0
for element in root.findall('.//artist'):


	artist = []
	artist_list = []
	if count == 0:
		# ID_number = member.find('ID_number').tag
		# discogs_head.append(ID_number)
		name = element.find('name').text 
		# discogs_head.append(name)
		# RealName = member.find('RealName').tag
		# discogs_head.append(RealName)
		# Profile = member.find('Profile').tag
		# discogs_head.append(Profile)
		# DataQuality = member.find('DataQuality').tag
		# discogs_head.append(DataQuality)
		# name_variations = memner.find('name_variations').tag
		# discogs_head.append(name_variations)
		# alias = member.find('alias').tag
		# csvwrter.writerow(discogs_head)
		# count = count + 1 

		print(name)



	discogs_data.close()