import re


def verification(content):
    # name starts with uppercase letter, followed by lovercase letters
    name_format = re.compile(r"First name: [A-Za-z]{2,25}\nLast name: [A-Za-z-]{2,25}")
    # phone nr exactly 10 digits
    phone_format = re.compile(r"Phone: \d{10}")
    # address: number, followed by street name
    address_format = re.compile(r"Address: \d{3}, [A-Za-z]{2,20} Street")
    # product name, price floating point nr, tva floating point nr + %, quantity: an integer number
    bill_format = re.compile(
        r"Service: (.+), Price: (\d+\.\d{2}), TVA: (\d+\.\d{2})%, Quantity: (\d+)"
    )

    errors = []

    if not name_format.search(content):
        errors.append("Error at client name.")

    if not phone_format.search(content):
        errors.append("Error at phone number.")

    if not address_format.search(content):
        errors.append("Error at address.")

    if not bill_format.search(content):
        errors.append("Error at service details.")
    return errors


path = input("Enter path: ")
with open(path, "r") as file:
    content = file.read()

errors = verification(content)

if not errors:
    print("The file respects the formatting requirements.")
else:
    print("The file does not respect the formatting requirements. Errors:")
    for error in errors:
        print(error)
