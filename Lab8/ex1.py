stack = []


def push(symbol):
    stack.append(symbol)


def pop():
    if len(stack) > 0:
        return stack.pop()
    else:
        return None


def pda(input):
    for symbol in input:
        # daca primeste 0, il pune in stive
        if symbol == "0":
            push(symbol)
        # daca primeste 1
        elif symbol == "1":
            # se elmina ultimul element adaugat si se verfica
            popped_symbol = pop()
            # daca este goala, sau continea un singur 0
            if popped_symbol == None or (popped_symbol == "0" and len(stack) == 0):
                return False
        else:
            print("Invalid symbol!")
            return False

    return len(stack) == 0


if pda("0011"):
    print("0011 is accepted")
else:
    print("0011 is not accepted")

if pda("0101"):
    print("0101 is accepted")
else:
    print("0101 is not accepted")
