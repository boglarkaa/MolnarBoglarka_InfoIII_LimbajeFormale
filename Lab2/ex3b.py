V = ["S", "X", "Y", "Z"]
T = ["0", "1", "2", "3", "4"]
P = {"S": "X", "X": ["0Y", "1Z"], "Y": ["2", "X"], "Z": ["3", "4", "X"]}

max_length = int(input("Enter max lenght: "))

words = ["S"]

while len(words[0]) <= max_length:
    new_words = []
    for word in words:
        for letter in word:
            for v in V:
                if letter == v:
                    for i in range(len(P[v])):
                        new_words.append(word.replace(letter, P[v][i], 1))
                        if (
                            len(new_words[-1]) == max_length
                            and new_words[-1][-1] not in V
                        ):
                            print(new_words[-1], end=" ")
    words = new_words
