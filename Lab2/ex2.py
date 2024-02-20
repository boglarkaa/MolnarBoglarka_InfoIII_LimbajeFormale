V = {"S", "A", "B"}
T = {"a", "b"}
P = ["aSa", "bSb", "a", "b"]

iterations = 3
result_words = ["S"]

for _ in range(iterations + 1):
    new_words = []
    for word in result_words:
        for production in P:
            new_words.append(word.replace("S", production, 1))
    print(set(result_words))
    result_words = new_words
