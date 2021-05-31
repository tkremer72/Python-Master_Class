# def multiply(x, y):
#     result = x * y
#     return result
#
#
# answer = multiply(10.5, 4)
# print(answer)
#
# print("*" * 5)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print("*" * 5)
#
# for val in range(1, 6):  # loops through the numbers 1 - 6 and stores
# them in
# val on each iteration
#     two_times = multiply(2, val)  # sets the value of two_times to the
#     value of multiplying 2 *
#     the current value of val
#     print(two_times)  # prints out the result
#
# print("*" * 5)


# def is_palindrome(string):
#     backwards = string[::-1] # slice reverses the string
#     return backwards == string


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    #  print(string)
    #   return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


word = input("Please enter a word to check: ")

if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
