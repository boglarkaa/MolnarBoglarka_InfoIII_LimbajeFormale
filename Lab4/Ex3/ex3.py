V = ["S", "A", "B"]
T = ["a", "b"]
P = {"S": ["aA", "bB"], "A": ["a", "bA", ""], "B": ["aB", ""]}

nr_of_words = int(input("Enter the number of words you want to generate: "))

words = ["S"]

while len(set(words)) < nr_of_words:
    new_words = []
    for word in words:
        for v in V:
            for x in P[v]:
                new_words.append(word.replace(v, x, 1))
    words = new_words

words = set(words)
print(words)

E = ["a", "b"]
Q = ["S0", "S1", "S2", "S3"]


def is_accepted(word):

    current_state = Q[0]
    final_state = Q[1]

    transitions = {
        # S0 a -> S2
        (Q[0], E[0]): Q[2],
        # S0 b -> S3
        (Q[0], E[1]): Q[3],
        # S2 a -> S1
        (Q[2], E[0]): Q[1],
        # S2 b -> S2
        (Q[2], E[1]): Q[2],
        # S3 a -> S3
        (Q[3], E[0]): Q[3],
        # S2 b -> S1
        (Q[3], E[1]): Q[1],
    }

    for letter in word:
        print(current_state + " " + letter)
        if (current_state, letter) in transitions:
            current_state = transitions[(current_state, letter)]
        else:
            return False

    return current_state == final_state


for word in words:
    if is_accepted(word):
        print(f"The word '{word}' is accepted")
    else:
        print(f"The word '{word}' is rejected")
