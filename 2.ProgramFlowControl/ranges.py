for i in range(1, 21):  # iterate over a range of numbers from 1 - 20
    print("i is now {}".format(i))  # print the value of i after each iteration
#  the curly braces represent a replacement variable, in this case it is the value of i
# when using range the starting number will be the actual value of the first number
# the ending number will be one less than the actual value of the second number.

# use a range to print a range of values a certain number of times, you don't need a start value
# if you don't provide a start value python defaults to 0
for x in range(21):
    print("x is now {}".format(x))

# using range with step
for y in range(0, 10, 2): # python interprets this as increasing by 2, so it counts 0 to 10 in increments of 2
    print("x is now {}".format(y))
# to count backwards the step must be a negative number
for y in range(10, 0, -2):
    print("y is now {}".format(y))

