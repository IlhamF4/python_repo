VOWELS = ('a','i','u','e','o','y')

def test_pig_latin_translator(translate_text):
    """
    Test function for Pig Latin translator
    Takes a function that accepts a string and returns the Pig Latin translation
    """
    # Test cases organized by category
    test_cases = {
        "Basic Words": [
            ("hello", "ello-hay"),              # Simple consonant start
            ("elephant", "elephant-yay"),        # Simple vowel start
            ("string", "ing-stray"),            # Consonant cluster
        ],
        
        "Capitalization": [
            ("Hello", "Ello-hay"),              # Title case
            ("HELLO", "ELLO-HAY"),              # All caps
            ("PyThOn", "y-thon-pay"),           # Mixed case
        ],
        
        "Punctuation": [
            ("hello!", "ello-hay!"),            # End punctuation
            ("'hello'", "'ello-hay'"),          # Surrounding punctuation
            ("hello?!", "ello-hay?!"),          # Multiple end punctuation
        ],
        
        "Numbers and Special Characters": [
            ("C3PO", "3po-cay"),               # Mixed letters and numbers
            ("2nd", "2nd-yay"),                 # Number prefix
            ("$$cash", "$$ash-cay"),            # Special character prefix 
        ],
        
        "Complex Cases": [
            ("well-known", "ell-way-own-knay"), # Hyphenated words
            ("I'm", "i'm-yay"),                 # Contractions
            ("U.S.A", "u.s.a-yay"),            # Acronyms with periods
            ("Hello, World!", "ello-hay, orld-way!"), # Full sentence
        ]
    }
    
    # Run tests and collect results
    results = []
    for category, cases in test_cases.items():
        print(f"\nTesting {category}:")
        for input_text, expected in cases:
            actual = translate_text(input_text)
            passed = actual.strip() == expected
            results.append(passed)
            print(f"Input: {input_text}")
            print(f"Expected: {expected}")
            print(f"Got: {actual}")
            print(f"{'✓ PASS' if passed else '✗ FAIL'}\n")
    
    # Summary
    total = len(results)
    passed = sum(results)
    print(f"\nTest Summary:")
    print(f"Passed: {passed}/{total} ({(passed/total*100):.1f}%)")
    
    return passed == total

# Helper function to wrap your existing code
def translate(word):
        prefixNonLetter = ""
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetter += word[0]
            word = word[1:]
        if len(word) == 0:
            return prefixNonLetter
            
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
            word += prefixConsonant + "-ay"
        else:
            word += "-yay"
                
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()
            
        return prefixNonLetter + word + suffixNonLetter

def translate_to_pig_latin(text):
    """Wrapper function for your Pig Latin translator"""
    pigLatin = []
    
    for word in text.split():
        if "-" in word:
        	parts = word.split("-")
        	translated_parts = [translate(part) for part in parts]
        	pigLatin.append("-".join(translated_parts))
        else:
        	pigLatin.append(translate(word))
    return " ".join(pigLatin)

# Run the tests
if __name__ == "__main__":
    print("Running Pig Latin Translator Tests...")
    all_passed = test_pig_latin_translator(translate_to_pig_latin)
    if all_passed:
        print("\nAll tests passed! Your translator is working perfectly!")
    else:
        print("\nSome tests failed. Check the results above to see which cases need attention.")