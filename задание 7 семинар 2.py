N = list(map(int, input().split()))
m = 0
for i in range(0, len(N)):
    if N.count(i) == 1:
        print(i)
