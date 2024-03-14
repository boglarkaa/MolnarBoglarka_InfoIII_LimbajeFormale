Q = ["Q1", "Q2"]
E = ["X", "Y"]
O = ["O1", "O2"]

trasitions = {
    ("Q1", "X"): ("Q2", "O1"),
    ("Q1", "Y"): ("Q1", "O1"),
    ("Q2", "X"): ("Q1", "O2"),
    ("Q2", "Y"): ("Q2", "O2"),
}


def print_state_and_output(state, input):
    if (state, input) in trasitions:
        print(
            "State "
            + state
            + " with input "
            + input
            + "results in state: "
            + trasitions[state, input][0]
            + " and output: "
            + trasitions[state, input][1]
        )
    else:
        print("Invalid state or input")


print_state_and_output(Q[0], E[0])
print_state_and_output(Q[0], E[1])
print_state_and_output(Q[1], E[0])
print_state_and_output(Q[1], E[1])
