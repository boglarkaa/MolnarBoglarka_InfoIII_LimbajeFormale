# varianta cu libraria regex

import re

cod = input("Cod postal: ")
# \d -> [0-9]
format = re.compile(r"^[1-9]\d{4}$")

if not format.match(cod):
    print("Incorrect")
else:
    print("Correct")

##############

# fara librarie regex


def validate(cod):
    if len(cod) != 5:
        return False
    if not (10 <= int(cod[:2]) <= 99):
        return False
    if not cod[2:].isdigit():
        return False

    return True


# Example usage:
cod = input("Cod postal: ")
if validate(cod):
    print("Correct")
else:
    print("Incorrect")
