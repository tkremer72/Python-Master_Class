flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
    "Peace Lily",
    "Daisy",
    "Rose",
    "Bluebell",
    "Orchid",
    "Poppy",
    "Marigold",
    "Honeysuckle",
    "Azalea",
    "Buttercup",
]

# for flower in flowers: # iterate over this list
#     print(flower) # print this list

separator = ", "  # create a variable to store a separator character
output = separator.join(flowers)  # Create a variable to store the joined list items and character
print(output)  # print output

# if you want to join iterables they must be strings

print(", ".join(flowers))  # does the same as the above code
print("*" * 45)

numbers = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
]

for number in numbers:
    print(", ".join(numbers))

print("*" * 45)

