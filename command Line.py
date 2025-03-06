#! python3
#mini clip
from kivy.core.clipboard import Clipboard
import sys

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}
        
if len(sys.argv) < 2:
	print('error')
	sys.exit()
keyphrase = sys.argv[1]
if keyphrase in TEXT:
	Clipboard.copy(TEXT[keyphrase])
	print("Text for "+ keyphrase +"has been copied")
else:
	print("There is no text for" + keyphrase)