import re

from lib.examples import efik_examples

print("\n=== (iii.) ===\n")


def test_efik_pattern(pattern_info):
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