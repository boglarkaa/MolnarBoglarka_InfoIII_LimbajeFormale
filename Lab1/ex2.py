A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
B = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k"]
C = ["x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4", "x5", "y5"]


def concat(s1, s2):
    return s2 + s1


def repeat(s, n):
    return s * n


def reverse(s):
    return s[::-1]


def extract(s, i, j):
    return s[i : j + 1]


def replace(s, sub, new_sub):
    s.replace(sub, new_sub, 1)


word = str(A[0]) + B[1] + C[2] + str(A[3]) + B[4] + C[5]

print(concat(word, str(A[1]) + B[2] + C[3]))
print(repeat(word, 5))
print(reverse(word))
print(extract(word, 2, 5))
print(replace(word, C[2], B[1]))
