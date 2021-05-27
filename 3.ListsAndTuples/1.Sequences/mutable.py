shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
print("*" * 75)
shopping_list += ["cookies"] # mutates the list
print(shopping_list)
print(id(shopping_list))
print(another_list)
print("*" * 75)

a = b = c = d = e = f = another_list
# a = another_list # lines 18 - 23 are the same as 17
# b = another_list
# c = another_list
# d = another_list
# e = another_list
# f = another_list

print(a)
print("*" * 75)

print("Adding cream")
b.append("cream")
print(c)
print("*" * 75)

print(d)
print("*" * 75)

print(e)
print("*" * 75)

print(f)
print("*" * 75)
