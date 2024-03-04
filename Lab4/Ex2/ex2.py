nr_of_slots = int(input("Enter number of slots: "))
empty_slots = nr_of_slots
taken_slots = 0

choice = ""

while choice != "D":
    choice = input(
        "Choose an option:\nA) Park a car\nB) Leave the parking lot\nC) Verify parking status\nD) OK\n"
    )

    if choice == "A":
        if empty_slots > 0:
            empty_slots -= 1
            taken_slots += 1
            print("Parked successfully!")
        elif taken_slots == nr_of_slots:
            print("There are no empty slots left!")
    elif choice == "B":
        if taken_slots == 0:
            print("There are no cars in the parking lot!")
        else:
            empty_slots += 1
            taken_slots -= 1
            print("Left parking lot successfully!")
    elif choice == "C":
        print(
            "Number of empty slots %d\nNumber of taken slots: %d"
            % (empty_slots, taken_slots)
        )
    elif choice == "D":
        print("Done!")
    else:
        print("Invalid choice!")
