import json
data = json.load(open('data.json'))

user_input = input("Enter country code: ")
user_input = "+" + str(user_input)

print

for country_record in data:
	for dial_num in country_record:
		if user_input == country_record[dial_num]:
			print "Name: " + str(country_record["name"])
			print "Code: " + str(country_record["code"])
			print "Dial Number: " + str(country_record["dial_code"])
