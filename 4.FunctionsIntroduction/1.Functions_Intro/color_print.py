import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def color_print(text: str, effect: str) -> None:
    """
    Print `text` using the ANSI sequences to change color, etc.

    :param text: The text to print.
    :param effect: The effect we want.  One of the constants defined at
        the start of this module.
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


colorama.init()
color_print("Hello Red!", RED)
# Test that the color was reset.
print("This should be in the default terminal color!")
color_print("Hello, Blue!", BLUE)
color_print("Hello, Yellow!", YELLOW)
color_print("Hello, Bold!", BOLD)
color_print("Hello, Underline!", UNDERLINE)
color_print("Hello, Reverse!", REVERSE)
color_print("Hello, Black!", BLACK)
colorama.deinit()
