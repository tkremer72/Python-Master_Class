letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1] # reverses the letters

print(backwards)
# slice the string to produce the letters qpo
print(letters[16:13:-1])
# slice that produces edbca
print(letters[4::-1])
# slice that produces the last 8 characters in reverse order
print(letters[:17:-1])
print(letters[:-9:-1])
# last four characters
print(letters[-4:])
# last letter
print(letters[-1:])
# first letter
print(letters[:1])
# first letter
print(letters[0])