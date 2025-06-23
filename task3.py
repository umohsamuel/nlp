



# Task 3: Regular Expression Analysis and Implementation
# (i.) Original Code Analysis

import re
import unicodedata
exp1 = re.compile(r'a+b+')
text = input("Please enter a string: ")
if exp1.match(text):
    print("Valid string")
else:
    print("Invalid string")

"""
EXPLANATION OF ORIGINAL CODE:
1. import re: Imports Python's regular expression library
2. exp1 = re.compile(r'a+b+'): Compiles a regex pattern that matches:
   - One or more 'a' characters (a+)
   - Followed by one or more 'b' characters (b+)
   - Examples: "ab", "aab", "abb", "aaabbb" are valid
   - Examples: "ba", "a", "b", "abc" are invalid
3. text = input(...): Gets user input
4. exp1.match(text): Checks if the string matches the pattern from the beginning
5. Prints "Valid" or "Invalid" based on match result
"""

# (ii.) Testing different regular expressions
print("\n=== TESTING DIFFERENT REGULAR EXPRESSIONS ===\n")

def test_regex(pattern, test_strings, description):
    """Helper function to test regex patterns"""
    print(f"Pattern: {pattern}")
    print(f"Description: {description}")
    compiled_pattern = re.compile(pattern)
    for test_str in test_strings:
        result = "Valid" if compiled_pattern.match(test_str) else "Invalid"
        print(f"  '{test_str}' -> {result}")
    print()

# (a) exp1 = re.compile(r'[01]')
test_regex(r'[01]', 
          ["0", "1", "2", "01", "10", ""], 
          "Matches a single binary digit (0 or 1)")

# (b) exp1 = re.compile(r'[A-Za-z]')
test_regex(r'[A-Za-z]', 
          ["A", "z", "1", "Ab", "hello", ""], 
          "Matches a single letter (uppercase or lowercase)")

# (c) exp1 = re.compile(r'[0-9]')
test_regex(r'[0-9]', 
          ["5", "a", "12", "9", "", "x"], 
          "Matches a single decimal digit")

# (d) exp1 = re.compile(r'[0-9]{2,4}')
test_regex(r'[0-9]{2,4}', 
          ["12", "1", "123", "1234", "12345", "ab"], 
          "Matches 2 to 4 decimal digits")

# (e) exp1 = re.compile(r'a[cde]*b')
test_regex(r'a[cde]*b', 
          ["ab", "acb", "acdeb", "aecb", "afb", "a"], 
          "Matches 'a', followed by zero or more c/d/e, then 'b'")

# (f) exp1 = re.compile(r'a[cde]?b')
test_regex(r'a[cde]?b', 
          ["ab", "acb", "adb", "aeb", "accb", "afb"], 
          "Matches 'a', optionally one c/d/e, then 'b'")

# (g) & (h) - Note: Variable substitution in regex strings
# For (g), Python doesn't substitute variables in raw strings directly
# We need to use f-strings or format
n = 2
pattern_g = f'a{{{n}}}b{{{n}}}'  # Creates 'a{2}b{2}'
test_regex(pattern_g, 
          ["aabb", "ab", "aaabbb", "aa", "bb"], 
          f"Matches exactly {n} 'a's followed by {n} 'b's")

# (h) exp1 = re.compile(r'a{2}b{2}')
test_regex(r'a{2}b{2}', 
          ["aabb", "ab", "aaabbb", "aa", "bb"], 
          "Matches exactly 2 'a's followed by 2 'b's")

# (i) exp1 = re.compile(r'a+b+') - Same as original
test_regex(r'a+b+', 
          ["ab", "aab", "abb", "aaabbb", "ba", "a", "b"], 
          "Matches one or more 'a's followed by one or more 'b's")

print("\n=== (iii.) EFIK LANGUAGE EXAMPLES ===\n")

"""
Efik Language Information:
- Efik is spoken in Cross River State and Akwa Ibom State, Nigeria
- Uses Latin script with some diacritical marks
- Has tone marks and special characters
- Common letters: a, b, d, e, ẹ, f, g, h, i, ị, k, m, n, ñ, o, ọ, p, r, s, t, u, ụ, w, y
"""

# Six examples for Efik language patterns
efik_examples = [
    {
        'pattern': r'[aeiọụẹị]+',
        'description': 'Matches one or more Efik vowels (including tone-marked vowels)',
        'test_words': ['aba', 'ọkọ', 'ịdịa', 'mme', 'consonant', 'ẹkẹ'],
        'meaning': 'Pattern for vowel sequences in Efik'
    },
    {
        'pattern': r'[kmnñpst]+[aeiọụẹị]+',
        'description': 'Consonant(s) followed by vowel(s) - basic Efik syllable structure',
        'test_words': ['ka', 'mme', 'nta', 'ñko', 'hello', 'sta'],
        'meaning': 'Basic CV (Consonant-Vowel) pattern'
    },
    {
        'pattern': r'(mme|eka|oro|ado)',
        'description': 'Common Efik words pattern',
        'test_words': ['mme', 'eka', 'oro', 'ado', 'house', 'other'],
        'meaning': 'Matches specific Efik words: mme(water), eka(one), oro(word), ado(place)'
    },
    {
        'pattern': r'[aeiọụẹị]{2,3}',
        'description': 'Two to three consecutive vowels (common in Efik)',
        'test_words': ['ịọ', 'ọọọ', 'eia', 'ai', 'consonant', 'a'],
        'meaning': 'Vowel clusters of 2-3 vowels'
    },
    {
        'pattern': r'ñ[aeiọụẹị]+[kpt]?',
        'description': 'Words starting with ñ (palatalized n) + vowels, optional final consonant',
        'test_words': ['ñak', 'ñia', 'ñọ', 'hello', 'mak', 'ñ'],
        'meaning': 'Efik words with palatalized n'
    },
    {
        'pattern': r'[ụụọọẹẹịị]+[bmn]',
        'description': 'Tone-marked vowels followed by nasal consonants',
        'test_words': ['ụọm', 'ẹẹn', 'ịịb', 'hello', 'an', 'ọn'],
        'meaning': 'Tonal vowel + nasal ending pattern'
    }
]

def test_efik_pattern(pattern_info):
    """Test Efik language patterns"""
    pattern = pattern_info['pattern']
    description = pattern_info['description']
    test_words = pattern_info['test_words']
    meaning = pattern_info['meaning']
    
    print(f"Pattern: {pattern}")
    print(f"Description: {description}")
    print(f"Meaning: {meaning}")
    
    compiled_pattern = re.compile(pattern)
    for word in test_words:
        result = "Valid" if compiled_pattern.match(word) else "Invalid"
        print(f"  '{word}' -> {result}")
    print()

# Test all Efik examples
for i, example in enumerate(efik_examples, 1):
    print(f"Example {i}:")
    test_efik_pattern(example)

print("=== EFIK LANGUAGE UNICODE DEMONSTRATION ===")
print("Common Efik words with Unicode characters:")
efik_words = [
    ("ñwed", "to write"),
    ("ọkọ", "husband/man"),
    ("ịdịa", "name"),
    ("ẹkẹ", "python/snake"),
    ("ụfọk", "house"),
    ("mme", "water")
]

for word, meaning in efik_words:
    print(f"  {word} - {meaning}")

# Example of comprehensive Efik word pattern
print("\n=== COMPREHENSIVE EFIK WORD PATTERN ===")
comprehensive_pattern = r'[kmnñpstbdgfhwy]?[aeiọụẹị]+[kmnñpstbdgfhwy]?'
test_regex(comprehensive_pattern,
          ["ñwed", "ọkọ", "ịdịa", "ẹkẹ", "ụfọk", "mme", "english"],
          "General Efik word structure: optional consonant + vowel(s) + optional consonant")



# Test Efik language patterns with Unicode characters

def test_efik_pattern(pattern_info):
    """Test Efik language patterns"""
    pattern = pattern_info['pattern']
    description = pattern_info['description']
    test_words = pattern_info['test_words']
    meaning = pattern_info['meaning']
    
    print(f"Pattern: {pattern}")
    print(f"Description: {description}")
    print(f"Meaning: {meaning}")
    
    compiled_pattern = re.compile(pattern)
    for word in test_words:
        result = "Valid" if compiled_pattern.match(word) else "Invalid"
        print(f"  '{word}' -> {result}")
    print()

# Test all Efik examples
for i, example in enumerate(efik_examples, 1):
    print(f"Example {i}:")
    test_efik_pattern(example)



    # IV 



    # Efik language examples with Unicode
efik_chars = {
    'ñ': 'n with tilde (palatalized n)',
    'ọ': 'o with dot below (open o)',
    'ẹ': 'e with dot below (open e)', 
    'ị': 'i with dot below',
    'ụ': 'u with dot below'
}

for char, description in efik_chars.items():
    unicode_name = unicodedata.name(char, 'UNKNOWN')
    unicode_code = f"U+{ord(char):04X}"
    print(f"  '{char}' - {description} - {unicode_name} - {unicode_code}")

# Efik words with Unicode
print("\nEfik Words with Unicode Support:")
efik_vocabulary = [
    ("ñwed", "to write", "demonstrates palatalized n"),
    ("ọkọ", "husband/man", "open o vowels"),
    ("ịdịa", "name", "dotted i vowels"),
    ("ẹkẹ", "python/snake", "open e vowels"),
    ("ụfọk", "house", "mixed vowel marks"),
    ("mmọñ", "child", "nasal + tonal vowels")
]

for word, meaning, note in efik_vocabulary:
    print(f"  {word:8} - {meaning:12} ({note})")
    
    # Analyze Unicode composition
    chars_info = []
    for char in word:
        chars_info.append(f"'{char}'(U+{ord(char):04X})")
    print(f"    Unicode: {' + '.join(chars_info)}")

# Regular expressions for Efik Unicode patterns
print("\nEfik Unicode Regular Expression Patterns:")
efik_patterns = {
    r'[ọụẹị]+': 'Tonal vowels (dotted vowels)',
    r'ñ[aeiọụẹị]+': 'Words starting with palatalized n',
    r'[aeiọụẹị]{2,}': 'Vowel clusters (2 or more vowels)',
    r'mm[ọụẹị]': 'Words with double m + tonal vowel'
}

test_words = ["ọkọ", "ñwed", "ịdịa", "ẹkẹ", "ụfọk", "mmọñ", "hello", "test"]

for pattern, description in efik_patterns.items():
    print(f"\nPattern: {pattern} ({description})")
    compiled_pattern = re.compile(pattern)
    for word in test_words:
        match = compiled_pattern.search(word)
        result = "✓" if match else "✗"
        matched_part = f" -> '{match.group()}'" if match else ""
        print(f"  {word:8} {result}{matched_part}")

# Unicode normalization for Efik
print("\n\nUnicode Normalization for Efik Text:")
efik_text = "Ñwed ụfọk ẹkẹ ọkọ ịdịa"
print(f"Original: {efik_text}")
print(f"NFC (Canonical): {unicodedata.normalize('NFC', efik_text)}")
print(f"NFD (Decomposed): {unicodedata.normalize('NFD', efik_text)}")

# Text processing with Unicode
print("\nText Processing with Efik Unicode:")
print(f"Length: {len(efik_text)} characters")
print(f"Byte length (UTF-8): {len(efik_text.encode('utf-8'))} bytes")

# Count special characters
special_chars = re.findall(r'[ñọẹịụ]', efik_text)
print(f"Special Efik characters found: {special_chars}")
print(f"Count of special characters: {len(special_chars)}")