import re
regex = r'^\d{1,3}(?:,\d{3})*$'

test_strings = [
    '42',           # Should match - 2 digits
    '1,234',        # Should match - 4 digits with comma
    '6,368,745',    # Should match - 7 digits with commas
    '12,34,567',    # Should NOT match - wrong comma placement
    '1234'          # Should NOT match - missing comma
]

for test in test_strings:
    if re.match(regex, test):
        print(f"'{test}' matches!")
    else:
        print(f"'{test}' does NOT match")