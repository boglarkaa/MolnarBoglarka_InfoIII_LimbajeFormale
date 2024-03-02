import re


def read_file():
    path = input("Enter path: ")
    with open(path, "r") as file:
        content = file.read()
    return content


def verification(content):

    # name starts with uppercase letter, followed by lovercase letters
    name_format = re.compile(r"Name: [A-Za-z]{2,25}\s[A-Za-z-]{2,25}")
    # phone nr exactly 10 digits
    phone_format = re.compile(r"Phone: \d{10}")
    # address: number, followed by street name
    address_format = re.compile(r"Address: \d{3}, [A-Za-z]{2,20} Street")
    # product name, price floating point nr, tva floating point nr + %, quantity: an integer number
    bill_format = re.compile(
        r"Product: (.+), Price: (\d+\.\d{2}), TVA: (\d+\.\d{2})%, Quantity: (\d+)"
    )

    errors = []

    match_name = name_format.search(content)
    if not match_name:
        errors.append("Error at client name.")

    match_phone = phone_format.search(content)
    if not match_phone:
        errors.append("Error at phone number.")

    match_address = address_format.search(content)
    if not match_address:
        errors.append("Error at address.")

    match_produs = bill_format.findall(content)
    if not match_produs:
        errors.append("Error at product details.")
    return errors


content = read_file()
errors = verification(content)

if not errors:
    print("The file respects the formatting requirements.")
else:
    print("The file does not respect the formatting requirements. Errors:")
    for error in errors:
        print(error)
