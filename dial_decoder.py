import json
data = json.load(open('data.json'))

user_input = input("Enter country code: ")
user_input = "+" + str(user_input)

print

found_results = []
for country_record in data:
	for dial_num in country_record:
		if user_input == country_record[dial_num]:
			found_results.append(country_record)

if not found_results:
	print "No matches."
else:
	print len(found_results), "result(s) found."
	print
	for result in found_results:
		print "Name: " + result["name"]
		print "Code: " + result["code"]
		print "Dial Number: " + result["dial_code"]
		print