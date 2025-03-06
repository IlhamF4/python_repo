print("Enter english text: ")
message = input()
VOWELS = ('a','i','u','e','o','y')
pigLatin = []

for word in message.split():
	prefixNonLetter = ""
	while len(word) > 0 and not word[0].isalpha():
		prefixNonLetter += word[0]
		word = word[1:]
	if len(word) == 0:
		pigLatin.append(prefixNonLetter)
		continue
		
	suffixNonLetter = ""
	while not word[-1].isalpha():
		suffixNonLetter = word[-1] + suffixNonLetter
		word = word[:-1]
		
	wasUpper = word.isupper()
	wasTitle = word.istitle()
	word = word.lower()
	
	prefixConsonant = ""
	while len(word) > 0 and not word[0] in VOWELS:
		prefixConsonant += word[0]
		word = word[1:]
		
	if prefixConsonant != "":
		word += prefixConsonant + "ay"
	else:
		word += "yay"
			
	if wasUpper:
		word = word.upper()
	if wasTitle:
		word = word.title()
		
	pigLatin.append(prefixNonLetter + word + suffixNonLetter)
print(" ".join(pigLatin))