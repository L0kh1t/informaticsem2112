N = list(map(int, input().split()))
N.insert(0, N.pop(len(N)-1))
print(N)
