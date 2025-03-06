#!python3

from kivy.core.clipboard import Clipboard
import re

#find phone number
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? #area code
	(\s|-|\.)? #separator
	(\d{3}) #first 3 digit
	(\s|-|\.)
	(\d{4}) #last 4 digit
	(\s*(ext|x|ext.)\s*(\d{2,5}))? #extensi
	)''',re.VERBOSE)

#find email
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+ #username
	@
	[a-zA-Z0-9.-]+ #domain
	(\.[a-zA-Z]{2,4})
	)''',re.VERBOSE)

#search from clipboard
text = str(Clipboard.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = "-".join([groups[1],groups[3],groups[5]])
	if groups[8] != "":
		phoneNum += " x" + groups[8]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

#paste to clipboard
if len(matches) > 0:
	Clipboard.copy("\n".join(matches))
	print('copied to clipboard')
	print("\n".join(matches))
else:
	print('no phone number or email found')
