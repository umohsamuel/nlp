
from utils.test_regex import test_regex

print("\n=== (ii.) ===\n")


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