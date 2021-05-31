import random


# Challenge, print a message if the user inputs an invalid entry
def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        #     print("{0} is not a valid number.".format(temp))
        print("{0} is not a valid number.".format(temp))


highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing.
#  modify game to use a while loop to allow the player to continue guessing if guess is wron
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0  # initialize to any number that isn't the answer
while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed the number!")
        break
    else:
        if guess < answer:
            print("Please guess higher!")
        else:
            print("Please guess lower!")
