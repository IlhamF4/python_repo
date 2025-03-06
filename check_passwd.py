#!python3
import re

#input password
text = "a123hklvuc"

def check_passwd(text):
	uppercase = re.compile(r'[A-Z]+')
	lowercase = re.compile(r'[a-z]+')
	number = r'\d+'
	if len(text) < 8:
		return False
	elif not re.search(uppercase, text):
		return False
	elif not re.search(lowercase,text):
		return False
	elif not re.search(number,text):
		return False
	return True
	

#TODO Check password

#print if strong or not
if check_passwd(text):
	print("It is a strong password")
else:
	print("It is a weak password")