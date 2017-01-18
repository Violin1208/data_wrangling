#Deborah Leem January 2016

import csv

#open the file in read only and in binary mode
#output of this function is stored in a variable called csvfile
csvfile = open ('data/data-text.csv', 'rb')
#read the open file as a csv file and output stored in a varioable reader
#csv.reader() returns each new line of the file as a list of data 
#reader = csv.reader(csvfile)

#saves as a dictionary
reader = csv.DictReader(csvfile)

for row in reader:
	print row

