choice = "-"
while choice != "0":
    if choice in "12345":  # review the in and not in video
        print("You chose {}".format(choice))
    else:
        print("Choose your option from the list below: ")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tHave Dinner")
        print("5:\tGo To Bed")
        print("0:\tExit")
    choice = input()
