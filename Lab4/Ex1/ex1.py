Q = ["A", "B"]
E = ["0", "1"]
input_sections = ["010", "110", "1001"]

transitions = {
    (Q[0], E[0]): Q[1],
    (Q[0], E[1]): Q[0],
    (Q[1], E[0]): Q[0],
    (Q[1], E[1]): Q[1],
}


def find_final_state(inp):
    current_state = Q[0]
    for letter in inp:
        if (current_state, letter) in transitions:
            current_state = transitions[(current_state, letter)]
    return current_state


for inp in input_sections:
    print(find_final_state(inp))
