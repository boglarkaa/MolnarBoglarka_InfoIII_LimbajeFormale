stack = []
input = ""


def check(input):
    input = input.replace(" ", "")

    if not input.isalnum() or len(input) < 15 or len(input) > 34:
        return False

    # primele 2 caractere litere -> country code
    if input[0:2].isalpha():
        stack.append(input[0:2])

    # 2 numere -> check digits
    if input[2:4].isdigit():
        stack.append(input[2:4])

    # restul -> caractere alfanumerice
    if input[5:].isalnum():
        stack.append(input[5:])

    # verificare checksum
    # transforma literele in numere
    input = input[4:] + input[0:4]
    input_digits = ""
    for char in input:
        if char.isdigit():
            input_digits += char
        else:
            input_digits += str(10 + ord(char) - ord("A"))
    # verifica mod 97
    return int(input_digits) % 97 == 1


ibans = ["RO49 AAAA 1B31 0075 9384 0000", "GB29 NWBK 6016 1331 9268 19"]
for iban in ibans:
    if check(iban):
        print("IBAN valid.")
    else:
        print("IBAN invalid")
