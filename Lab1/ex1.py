A=['a', 'b', 'c']
B=['x', 'y', 'z']
C=[1, 2, 3]

def concatenate(s1, s2):
    return s1+s2

def invers(s):
    return s[::-1]

def substituie(s,a,b):
    return s.replace(a, b)

def lungime(s):
    return len(s)

print(concatenate(A[0]+A[1], B[2]))
print(invers(A[2]+B[1]+A[0]))
print(substituie(A[0]+A[1]+A[1], A[1], str(C[2])))
print(lungime(A[0]+B[1]+str(C[2])))

    
    
