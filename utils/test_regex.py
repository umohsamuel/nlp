import re

def test_regex(pattern, test_strings, description):
    print(f"Pattern: {pattern}")
    print(f"Description: {description}")
    compiled_pattern = re.compile(pattern)
    for test_str in test_strings:
        result = "Valid" if compiled_pattern.match(test_str) else "Invalid"
        print(f"  '{test_str}' -> {result}")
    print()