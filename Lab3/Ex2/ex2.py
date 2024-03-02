import itertools
import random

E = ["a", "b", "c", "d"]

pattern = ["".join(permutation) for permutation in itertools.permutations(E, 3)]

words = []
for word in pattern:
    if len(word + word) <= 6:
        words.append(word + word)

print("The generated words are:")
print(words)


def is_accepted(word):

    current_state = "q0"
    final_state = "q3"

    transitions = {
        ("q0", "a"): "q1",
        ("q0", "b"): "q0",
        ("q0", "c"): "q0",
        ("q0", "d"): "q0",
        ("q1", "a"): "q1",
        ("q1", "b"): "q2",
        ("q1", "c"): "q1",
        ("q1", "d"): "q1",
        ("q2", "a"): "q2",
        ("q2", "b"): "q2",
        ("q2", "c"): "q2",
        ("q2", "d"): "q2",
        ("q3", "a"): "q3",
        ("q3", "b"): "q3",
        ("q3", "c"): "q3",
        ("q3", "d"): "q3",
    }

    for letter in word:
        if (current_state, letter) in transitions:
            current_state = transitions[(current_state, letter)]
        else:
            return False

    return current_state == final_state


for _ in range(0, 3):
    word_to_check = words[random.randint(0, len(words) - 1)]
    if is_accepted(word_to_check):
        print(f"The word '{word_to_check}' is accepted")
    else:
        print(f"The word '{word_to_check}' is rejected")
