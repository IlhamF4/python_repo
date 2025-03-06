import re

text = [
	    'Haruto Watanabe',
    'Alice Watanabe',
    'RoboCop Watanabe',

    'haruto Watanabe', #(where the first name is not capitalized)
    'Mr. Watanabe', #(where the preceding word has a nonletter character)
    'Watanabe', #(which has no first name)
    'Haruto watanabe', #(where Watanabe is not capitalized)
]

regex = r'^[A-Z]\w*\sWatanabe$'
for group in text:
	if re.match(regex, group):
		print(f"{group} match")
	else:
		print(f"{group} does not match")