name = input("Please enter your name: ")
age = int(input("How old are you? "))

#  if age >= 18 and age < 31:
if 18 <= age < 31:
    print("Welcome to club holidays 18-30, {0}".format(name))
else:
    print("I am so sorry, you are not invited on this holiday.")