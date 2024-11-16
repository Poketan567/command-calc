import os

# The function that makes the terminal clear.
def clear_term():
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")