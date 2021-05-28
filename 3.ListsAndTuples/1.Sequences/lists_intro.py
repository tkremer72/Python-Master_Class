computer_parts = [
    "computer",  # index 0
    "monitor",   # index 1
    "keyboard",  # index 2
    "mouse",     # index 3
    "mouse pad"  # index 4
]

# for part in computer_parts:
#     print(part)
# print()
# print(computer_parts[2])  # returns index 2 which is keyboard
# print()
# print(computer_parts[0:3])  # returns a list from a list
# print()
# print(computer_parts[-1])  # returns the last item in the index

print(computer_parts)

#  computer_parts[3] = "trackball"
print(computer_parts[3:])
computer_parts[3:] = ["trackball"]
print(computer_parts)
