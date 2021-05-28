menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "sausage", "bacon", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

# Solution 1, remove spam from each of the inner lists
# for meal in menu: # iterate through the meals in the menu
#     for index in range(len(meal) - 1, - 1, -1): # iterate through the items in the meals backwards
#         if meal[index] == "spam":  # find all the items that are spam
#             del meal[index] # remove the items with spam
#     print(meal) # print on this indention level prints the meals after the loops finish

# Solution 2
# for meal in menu:  # iterate through the menu to get the meals
#     for item in meal:  # iterate through the items in the meals
#         if item != "spam":  # make sure that spam is not spam
#             print(item, end=", ")  # print the items that are not spam
#     print()  # Put a space between each meal

# The join method
for meal in menu:
    for index in range(len(meal) - 1, -1, - 1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))
