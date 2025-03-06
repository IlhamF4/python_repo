#! python3
#mini clip
from kivy.core.clipboard import Clipboard

text = Clipboard.paste()
"""do something here
"""
line = text.split("\n")
for i in range(len(line)):
	line[i] = "* " + line[i]
text = "\n".join(line)
Clipboard.copy(text)