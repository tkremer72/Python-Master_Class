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

# data = [] # no values test case



min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, - 1, - 1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]
# print(data)

#  Using the reversed function
top_index = len(data) - 1

for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
print(data)