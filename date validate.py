#!python3
import re
month = ""
day = ""
year = ""
days = [4,6,9,11]

def is_leapyear(year):
	return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def is_valid(month, day, year):
	if month in days and day > 30:
		return False
	if month == 2:
		 if is_leapyear(year) and day > 29:
		 	return False
		 elif is_leapyear(year) == False and day > 28:
		 	return False
	return True

#detect date
text = "02/30/2000"
regex = re.compile(r'''
	(0[1-9]|1[0-2]) #month
	/ #separator
	(0[1-9]|[1-2]\d|3[0-1]) #day
	/
	([1-2]\d{3})
''',re.VERBOSE)
#store variable
for group in regex.findall(text):
	month = int(group[0])
	day = int(group[1])
	year = int(group[2])
#check valid date
print(is_valid(month,day,year))



"""improved code
#!python3
import re

def is_leapyear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def is_valid(month, day, year):
    # Define month lengths
    thirty_day_months = [4, 6, 9, 11]  # April, June, September, November
    thirty_one_day_months = [1, 3, 5, 7, 8, 10, 12]  # January, March, May, July, August, October, December
    
    # Check basic month validity
    if month not in thirty_day_months and month not in thirty_one_day_months:
        return False
    
    # Check day validity based on month
    if month in thirty_day_months and day > 30:
        return False
    elif month in thirty_one_day_months and day > 31:
        return False
    elif month == 2:  # February special case
        if is_leapyear(year) and day > 29:
            return False
        elif not is_leapyear(year) and day > 28:
            return False
    
    return True

def validate_date(text):
    # Regular expression to detect dates in DD/MM/YYYY format
    date_regex = re.compile(r'''
     #   (0[1-9]|1[0-2])        # month (01-12)
   #     /                       # separator
   #     (0[1-9]|[1-2]\d|3[0-1]) # day (01-31)
 #       /                       # separator
#        ([1-2]\d{3})           # year (1000-2999)
    ''', re.VERBOSE)
    
    match = date_regex.search(text)
    if match:
        month = int(match.group(1))
        day = int(match.group(2))
        year = int(match.group(3))
        
        if is_valid(month, day, year):
            return f"{month:02d}/{day:02d}/{year} is a valid date."
        else:
            return f"{month:02d}/{day:02d}/{year} matches the date format but is not a valid calendar date."
    else:
        return "No valid date format found."

# Test cases
test_cases = [
    "02/30/2000",  # Invalid: February 30 in leap year
    "04/30/2023",  # Valid: April 30
    "04/31/2023",  # Invalid: April 31
    "02/29/2023",  # Invalid: February 29 in non-leap year
    "02/29/2024",  # Valid: February 29 in leap year
    "01/31/2023",  # Valid: January 31
    "Not a date"   # Invalid format
]

for test in test_cases:
    print(f"Testing '{test}': {validate_date(test)}")
""""