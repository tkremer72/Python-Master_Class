def fizz_buzz(number: int) -> str:
    """
    Play fizz buzz
    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3. 'buzz' if the number
        is divisible by 5.  'fizz buzz' if it is divisible by 3 and 5.
        The number, as a string, otherwise.
    """

    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


# for loop for testing purposes.
for i in range(1, 101):
    print(fizz_buzz(i))
