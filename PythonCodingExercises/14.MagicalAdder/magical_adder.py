# Get the user input
user_input = input("Please enter three numbers: ")

# Split input into 3 parts
strings_entered = user_input.split(",")

# convert strings to integers
int_created = []
for st in strings_entered:
    int_created.append(int(st))

# calculate the result
a, b, c = int_created
result = a + b - c
# result = int_created[0] + int_created[1] - int_created[2]
# output the result
print(result)
