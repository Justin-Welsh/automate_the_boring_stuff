"""
Does not work in the DAY/MONTH/YEAR format as asked for in the book.
It also does not check if the date is valid or not
"""



import re

def find_dates(list_of_dates):
	date_detector = re.compile(r'''
	([0-3][0-9]) 						# month - Any two digits between 00 and 39
	\/
	([0-1][0-9]) 						# day - Any two digits between 01 and 19
	\/
	([1-2][0-9][0-9][0-9]) 				# year - any four digits between 1000 and 2999
	''', re.VERBOSE)

	mo = date_detector.findall(list_of_dates)

	# Loop through the tuples given by findall()
	for i in range(len(mo)):
		day = mo[i][0]
		month = mo[i][1]
		year = mo[i][2]
		
		full_date = ""
		full_date = full_date.join(day + "/" + month + "/" + year)

		# Months can't be larger than 13
		if day.startswith("3"):
			if int(month[1]) > 2:
				print("No valid date found.")
				continue
		
		# Days can't be larger than 32
		if month.startswith("1"):
			if int(day[1]) > 2:
				print("No valid date found.")
				continue
		
		# Years can't be larger than 2020
		if int(year) > 2020:
			print("No valid dates.")
		else:
			print(f"Date found: {full_date}")

		# TODO: Check date to see if it's valid

dates = input("Enter a list of potential dates: ")
find_dates(dates)
