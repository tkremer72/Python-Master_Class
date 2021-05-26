number = input("Please enter a series of numbers, using any separators you like: ")

separators = ""  # We initialize this here because we need to keep track of values stored in separators
# in order to do this we need to create the word separators by defining a value with it

for char in number:
    if not char.isnumeric():  # loop through the string and pull the characters
        # that are separators and add them to the list of separators
        separators = separators + char  # only executed when a separator is found

# print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
