from random import randint
L = list(map(int, input().split()))


def quick_sort(N):
    s = len(N)
    if s == 1:
        return N
    if s == 0:
        return N
    n = randint(0, s - 1)
    x1 = []
    x2 = []
    x3 = []
    for i in range(s):
        if N[i] < N[n]:
            x1 += [N[i]]
        if N[i] == N[n]:
            x2 += [N[i]]
        if N[i] > N[n]:
            x3 += [N[i]]
    return quick_sort(x1) + x2 + quick_sort(x3)


print(quick_sort(L))
