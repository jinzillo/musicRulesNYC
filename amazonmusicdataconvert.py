import re
tsv = open('amazonmusicdata.tsv', 'r')
fileContent =  tsv.read()
fileContent = re.sub("\t", ",", fileContent) # convert from tab to comma
csv_file = open("amazonmusicdata.csv", "w")
csv_file.write(fileContent)
csv_file.close()