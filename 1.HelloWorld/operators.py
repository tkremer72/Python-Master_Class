a = 12
b = 3

#  Expressions below
print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 Integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder after integer division

print()         # Print a blank line

print(a + b / 3 - 4 * 12) # wrong
print()
print(a + (b / 3) - (4 * 12)) # wrong
print()
print((((a+b)/3 ) - 4) * 12) # right
print()
print(((a + b) / 3 - 4) * 12) # also right
print()
# or you could do the above with variables

c = a + b # 15
d = c / 3 # 5
e = d - 4 # 1
print(e * 12) # 12

print()

print(a / (b * a) / b) # equats to 12/36 /3