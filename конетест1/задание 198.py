N = [0] + list(map(int, input().split()))
b = [0]*(len(N))
for i in range(1, len(N)):
    b[i] = N[i] + max(b[i-2], b[i-3])
print(max(b[-1], b[-2]))

