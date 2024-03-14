E = ["a", "b", "E"]
Q = ["q0", "q1", "q2", "q3", "q4"]

transitions = {
    ("a", "q0"): "q1",
    ("a", "q1"): "q1",
    ("E", "q1"): "q2",
    ("b", "q2"): "q2",
    ("b", "q2"): "q3",
    ("a", "q2"): "q3",
    ("a", "q3"): "q3",
    ("b", "q3"): "q1",
    ("E", "q3"): "q4",
}


def check(word):
    current_state = Q[0]
    final_state = Q[4]
    for letter in word:
        if (letter, current_state) in transitions:
            current_state = transitions[letter, current_state]
            print(current_state)
        else:
            print("Error")
    return final_state == current_state


print(check("aba"))
print(check("aEaaE"))
