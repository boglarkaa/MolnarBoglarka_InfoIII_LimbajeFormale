E = ["C", "T", "A", "H", "OK"]
Q = ["q0", "q1", "q2", "q3", "q4"]

state = Q[0]

while state == Q[0]:
    print(
        "Choose a drink!\nType:\nC for Coffee\nT for Tea\nA for Cappuccino\nH for Hot Choco"
    )
    choice = input()
    while choice not in E:
        choice = input("Invalid input. Choose something else.\n")
    if choice == E[0]:
        state = Q[1]
    elif choice == E[1]:
        state = Q[2]
    elif choice == E[2]:
        state = Q[3]
    elif choice == E[3]:
        state = Q[4]
    print("You chose : " + choice)
    c = input("To confirm type OK.\n")
    while c != E[4]:
        c = input("Invalid input. To confirm type OK.\n")
    state = Q[4]
    if state == Q[4]:
        c = input("To select another drink type OK.\n")
        while c != E[4]:
            c = input("Invalid input. To select another drink type OK.\n")
        state = Q[0]
