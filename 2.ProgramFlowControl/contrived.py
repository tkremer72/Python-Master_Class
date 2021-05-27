numbers = [1, 45, 31, 12, 60]

for number in numbers:
    if number % 8 == 0:  # check to see if the number is exactly divisible by 8, if it is print the statement and
        # break out of loop
        # Reject the list
        print("The numbers are unacceptable!")
        break
else:
    print("All those numbers are fine!")
