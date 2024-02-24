V = ["S", "A", "B"]
T = ["a", "b"]
P = {"S": "AB", "A": "aA", "B": "bB"}

max_length = int(input("Enter max lenght: "))

words = ["S"]

keys = list(P.keys())


while len(words[0]) <= max_length + 1:
    new_words = []
    for word in words:
        for letter in word:
            for v in V:
                if letter == v:
                    new_words.append(word.replace(letter, P[v], 1))
    words = new_words

words = [word.replace("A", "").replace("B", "") for word in words]

print(set(words))
