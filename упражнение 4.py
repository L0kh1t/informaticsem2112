N = list(map(int, input()))
for i in range(0, len(N)-1, 2):
    N[i], N[i+1] = N[i+1], N[i]
    