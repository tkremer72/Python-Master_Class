shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "albatross"
found_at = None

# for index in range(6)
# for index in range(len(shopping_list)): # checks if the index is within the range of the length of the list
#     if shopping_list[index] == item_to_find: # if the index in the list is equal to item_to_find
#         found_at = index # return the index of where that item was found
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
