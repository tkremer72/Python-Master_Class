answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())
if guess == answer:
    print("You guessed the number on your first try!")
else:
    if guess < answer:
        print("Please guess higher!")
    else:
        print("Please guess lower!")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed the number!")
    else:
        print("Sorry, you have not guessed correctly!")

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher!")
#     else:  # guess must be greater than answer
#         print("Please guess lower!")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed the number!")
#     else:
#         print("Sorry you have not guessed correctly!")
# else:
#     print("You got it on your first try!")


# if guess < answer:
#     print("Please guess higher!")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry you have not guessed correctly!")
# elif guess > answer:
#     print("Please guess lower!")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry you have not guessed correctly!")
# else:
#     print("You guessed the number on your first try!")