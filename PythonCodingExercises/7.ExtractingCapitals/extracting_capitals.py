quote = """
Alright, but apart from the Sanitation, the Medicine,
    Education, Wine, 
Public Order, Irrigation, Roads, the Fresh-Water System, 
and Public Health, what have the Romans ever done for us?
"""
# use a for loop and an if statement to print just the capital letters
# in the quote above.
for char in quote:
    if char.isupper():
        print(char)
print("*" * 5)
# use a for loop and an if statement to print just the capital letters
# in the quote above.

for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char)

