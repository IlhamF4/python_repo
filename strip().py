import re

text ='   ada aku.   '
def dummy(text,cut="zero"):
	word = re.compile(f"[^{cut}]")
	space = re.compile(r'^\s+|\s$')
	new_text = ""
	if cut == "zero":
		new_text = re.sub(space, "", text)
	else:
		new_text = "".join(word.findall(text))
		print(new_text)
	return new_text
	
print(dummy(text))