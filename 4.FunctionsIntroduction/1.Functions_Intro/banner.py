# Function that creates a banner neatly formatted text
def banner_text(text=" ", screen_width=80):
    """ Print a string centered, with ** either side.

    :param text:  The string to print.
    An asterisk (*) will result in a row of asterisks.
    The default will print a blank line, with a ** border at
    the left and right edges.
    :param screen_width: The overall width to print within (including
    the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    # screen_width = 50
    if len(text) > screen_width - 4:  # Check to make sure the text isn't too long, if it is print below or carry on
        # print("EEK!!", 60)
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH!", 60)
        raise ValueError("String {0} is larger then the specified width {1}"
                         .format(text, screen_width))

    if text == "*":  # look for asterisks, if there are some, multiply them by the width and print them
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)  # center the text
        output_string = "**{0}**".format(centered_text)  # add asterisks on both sides
        print(output_string)  # print text with asterisks


banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 60)
banner_text("And... always look on the bright side of life...", 60)
banner_text("*", 60)
