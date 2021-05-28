a = b = c = d = e = f = 42
print(c)

print("*" * 5)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("*" * 5)

print("Unpacking A Tuple:")
data = 1, 2, 76 # data represents tuple
x, y, z = data
print(x)
print(y)
print(z)

print("*" * 5)

print("Unpacking A List")
data_list = [12, 13, 14]
#  data_list.append(15) #  can't do this, tuples are immutable
p, q, r = data_list
print(p)
print(q)
print(r)

print("*" * 5)

string_data = ["one", "two", "three"]
s, t, u = string_data
print(s)
print(t)
print(u)

print("*" * 5)
