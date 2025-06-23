print("\n=== (i.) ===\n")


import re
exp1 = re.compile(r'a+b+')
text = input("Please enter a string: ")
if exp1.match(text):
    print("Valid string")
else:
    print("Invalid string")

