import re
import unicodedata

from utils.test_regex import test_regex
from lib.examples import efik_examples


print("\n=== (iv.) ===\n")

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

print("\n=== COMPREHENSIVE EFIK WORD PATTERN ===")
comprehensive_pattern = r'[kmnñpstbdgfhwy]?[aeiọụẹị]+[kmnñpstbdgfhwy]?'
test_regex(comprehensive_pattern,
          ["ñwed", "ọkọ", "ịdịa", "ẹkẹ", "ụfọk", "mme", "english"],
          "General Efik word structure: optional consonant + vowel(s) + optional consonant")




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

for i, example in enumerate(efik_examples, 1):
    print(f"Example {i}:")
    test_efik_pattern(example)






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