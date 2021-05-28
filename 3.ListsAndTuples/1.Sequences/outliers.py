data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360] # Normal test case

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]  # Remove outlying values from end test case

# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360] # remove outlying values from start test case

# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191] # no outlying values to test

# data = [1041, 1051, 1101, 1201, 1301, 1301, 1501,
#         1601, 1701, 1831, 1851, 1871, 1881, 1911]  # no values within the range wanted test

#  data = [] # no values test case


# del data[0:2]
# print(data)
#
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# for index, value in enumerate(data):
#     if(value < min_valid) or (value > max_valid):
#         del data[index]  #  wrong

# process the low values of the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # For debugging

del data[:stop]
print(data)

#  process the high values of the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        #  We have the index of the last item to keep
        #  Set 'start' to the position of the first
        #  item to delete, which is 1 after 'index'
        start = index + 1
        break

print(start)  # for debugging

del data[start:]
print(data)
