import json

#read the file and store in the jason_data varioable
json_data = open('data/data-text.json').read()
#jason.loads() load JASON into Python
data = json.loads(json_data)

for item in data:
	print item

