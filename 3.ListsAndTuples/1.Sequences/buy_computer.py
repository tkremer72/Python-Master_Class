available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse pad",
                   "hdmi cable",
                   "dvd drive",
                   "memory",
                   "webcam",
                   "speakers",
                   "microphone",
                   "headset"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
# print(valid_choices)
current_choice = "-"
computer_parts = []  # Create an empty list
while current_choice != "0":
    #    if current_choice in "123456":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # already there, remove it.
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
        # if current_choice == '1':
        #     computer_parts.append("computer")
        # elif current_choice == '2':
        #     computer_parts.append("monitor")
        # elif current_choice == '3':
        #     computer_parts.append("keyboard")
        # elif current_choice == '4':
        #     computer_parts.append("mouse")
        # elif current_choice == '5':
        #     computer_parts.append("mouse pad")
        # elif current_choice == '6':
        #     computer_parts.append("hdmi cable")
    else:
        # print("Please add options from the list below: ")
        # print("1: computer")
        # print("2: monitor")
        # print("3: keyboard")
        # print("4: mouse")
        # print("5: mouse pad")
        # print("6: hdmi cable")
        # print("0: to exit")
        # for part in available_parts:
        #     print("{0}: {1}".format(available_parts.index(part) + 1, part))
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):  # use the enumerate function to get the part and the index
            # below we use replacement for the number and the part
            print("{0}: {1}".format(number + 1, part))  # add 1 to the index to get the correct list number
    current_choice = input()
print(computer_parts)
