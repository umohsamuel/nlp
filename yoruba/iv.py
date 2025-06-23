import re
import unicodedata

from utils.test_regex import test_regex
from lib.examples import yoruba_examples


print("\n=== (iv.) ===\n")

print("Common Yoruba words with Unicode characters:")
yoruba_words = [
    ("ọmọ", "child"),
    ("ilé", "house"),
    ("omi", "water"),
    ("ẹja", "fish"),
    ("àgbà", "elder"),
    ("ẹkọ", "lesson/corn meal"),
    ("gbọ", "to hear"),
    ("wọ", "to enter"),
    ("yẹ", "to be suitable"),
    ("kpẹ", "to be complete")
]

for word, meaning in yoruba_words:
    print(f"  {word} - {meaning}")

print("\n=== COMPREHENSIVE YORUBA WORD PATTERN ===")
comprehensive_pattern = r'[bdfghjklmnprstwygb]*[aeiouẹọàáèéìíòóùú]+[bdfghjklmnprstwygb]*'
test_regex(comprehensive_pattern,
          ["ọmọ", "ilé", "omi", "ẹja", "àgbà", "gbọ", "wọ", "english"],
          "General Yoruba word structure: optional consonant(s) + vowel(s) + optional consonant(s)")


def test_yoruba_pattern(pattern_info):
    """Test Yoruba language patterns"""
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

for i, example in enumerate(yoruba_examples, 1):
    print(f"Example {i}:")
    test_yoruba_pattern(example)


print("\n=== YORUBA UNICODE CHARACTER ANALYSIS ===")

yoruba_chars = {
    'ẹ': 'e with dot below (open e)',
    'ọ': 'o with dot below (open o)',
    'à': 'a with grave accent (low tone)',
    'á': 'a with acute accent (high tone)',
    'è': 'e with grave accent (low tone)',
    'é': 'e with acute accent (high tone)',
    'ì': 'i with grave accent (low tone)',
    'í': 'i with acute accent (high tone)',
    'ò': 'o with grave accent (low tone)',
    'ó': 'o with acute accent (high tone)',
    'ù': 'u with grave accent (low tone)',
    'ú': 'u with acute accent (high tone)',
    'ẹ̀': 'open e with grave accent (low tone)',
    'ẹ́': 'open e with acute accent (high tone)',
    'ọ̀': 'open o with grave accent (low tone)',
    'ọ́': 'open o with acute accent (high tone)'
}

for char, description in yoruba_chars.items():
    try:
        unicode_name = unicodedata.name(char, 'UNKNOWN')
        unicode_code = f"U+{ord(char):04X}"
        print(f"  '{char}' - {description} - {unicode_name} - {unicode_code}")
    except Exception as e:
        # Handle composite characters
        print(f"  '{char}' - {description} - COMPOSITE CHARACTER")

print("\nYoruba Words with Unicode Support:")
yoruba_vocabulary = [
    ("ọmọ", "child", "open o vowels"),
    ("ilé", "house", "high tone e"),
    ("omi", "water", "basic vowels"),
    ("ẹja", "fish", "open e vowel"),
    ("àgbà", "elder", "low tone a, gb digraph"),
    ("gbọ", "to hear", "gb digraph + open o"),
    ("wọlé", "come in", "compound word"),
    ("kò", "not/no", "low tone open o")
]

for word, meaning, note in yoruba_vocabulary:
    print(f"  {word:8} - {meaning:12} ({note})")
    
    # Analyze Unicode composition
    chars_info = []
    for char in word:
        chars_info.append(f"'{char}'(U+{ord(char):04X})")
    print(f"    Unicode: {' + '.join(chars_info)}")

# Regular expressions for Yoruba Unicode patterns
print("\nYoruba Unicode Regular Expression Patterns:")
yoruba_patterns = {
    r'[ẹọ]+': 'Open vowels (ẹ and ọ)',
    r'[àáèéìíòóùú]+': 'Tone-marked vowels',
    r'gb[aeiouẹọ]+': 'GB digraph words',
    r'[aeiouẹọ]{2,}': 'Vowel clusters (hiatus)',
    r'[yw][aeiouẹọ]+': 'Semi-vowel initial words',
    r'kp[aeiouẹọ]+': 'KP labio-velar sounds'
}

test_words = ["ọmọ", "ilé", "omi", "ẹja", "àgbà", "gbọ", "wọ", "yẹ", "kpẹ", "hello", "test"]

for pattern, description in yoruba_patterns.items():
    print(f"\nPattern: {pattern} ({description})")
    compiled_pattern = re.compile(pattern)
    for word in test_words:
        match = compiled_pattern.search(word)
        result = "✓" if match else "✗"
        matched_part = f" -> '{match.group()}'" if match else ""
        print(f"  {word:8} {result}{matched_part}")

# Unicode normalization for Yoruba
print("\n\nUnicode Normalization for Yoruba Text:")
yoruba_text = "Ọmọ mi wọlé, ẹja ní omi"
print(f"Original: {yoruba_text}")
print(f"NFC (Canonical): {unicodedata.normalize('NFC', yoruba_text)}")
print(f"NFD (Decomposed): {unicodedata.normalize('NFD', yoruba_text)}")

# Text processing with Unicode
print("\nText Processing with Yoruba Unicode:")
print(f"Length: {len(yoruba_text)} characters")
print(f"Byte length (UTF-8): {len(yoruba_text.encode('utf-8'))} bytes")

# Count special characters
special_chars = re.findall(r'[ẹọàáèéìíòóùú]', yoruba_text)
print(f"Special Yoruba characters found: {special_chars}")
print(f"Count of special characters: {len(special_chars)}")

# Tone analysis
print("\nTone Analysis:")
low_tone = re.findall(r'[àèìòù]', yoruba_text)
high_tone = re.findall(r'[áéíóú]', yoruba_text)
mid_tone = re.findall(r'[aeiou](?![́̀])', yoruba_text)  # Unmarked vowels (mid tone)

print(f"Low tone vowels: {low_tone} (count: {len(low_tone)})")
print(f"High tone vowels: {high_tone} (count: {len(high_tone)})")
print(f"Mid tone vowels: {mid_tone} (count: {len(mid_tone)})")