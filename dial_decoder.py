import json
from beautifultable import BeautifulTable

def is_number(s):
	while s.isdigit() == False:
		s = raw_input("Enter only numbers: ")
	return int(s)

data = json.load(open('data.json'))
table = BeautifulTable()

user_input = is_number(raw_input("Enter country code: "))
user_input = "+" + str(user_input)

print

found_results = []
for country_record in data:
	if user_input == country_record['dial_code']:
		found_results.append(country_record)

if not found_results:
	print "No matches."
else:
	print len(found_results), "result(s) found."
	print
	for result in found_results:
		table.column_headers = ["Name", "Code", "Dial"]
		table.append_row([result["name"], result["code"], result["dial_code"],])
	print table