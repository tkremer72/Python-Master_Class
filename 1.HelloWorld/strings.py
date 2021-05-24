print("Today is a good day to learn Python.")
print('Python is fun.')
print("Python's string are easy to use.")
print('We can even include "quotes" in strings.')

print("Hello" + " world!" + " This is done with string concatenation, this is where python" + " adds multiple strings" +
      " together in" + " one line.")
print()
# prints a blank line

# Comments need a hash in from of them, below we begin using variables even though we don't discuss them
greeting = "Hello"
# name = input("Please enter your name: ")  # the input function displays the text entered into it.
name = "Thomas"
print(greeting + name)
# if we want a space we can add that too
print(greeting + " " + name)
print()

age = 24
print(age)

print()

print(type(greeting))
print(type(age))
# rebind a value to a variable
age_in_words = "2 years"
print(name + f" is {age} years old") # using f string you can make this work
print(type(age_in_words))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
