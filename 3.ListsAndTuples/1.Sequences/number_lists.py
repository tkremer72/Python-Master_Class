empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
# print(numbers)

for number_list in numbers:  # iterates over each item in the list of lists and assigns them to number_list
    print(number_list)

    for value in number_list:  # iterates over each item in number_list and prints the value
        print(value)
