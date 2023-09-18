A = list(map(str, input().split()))
d = int(A[0])
A = A[1]
S = ''
while len(A) > 0:
    print(str(A[0: d-1])[::-1])
    S += str(A[0:d-1][::-1])
    A = A[d-1:]
print(S)
