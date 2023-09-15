N = list(map(int, input().split()))
a = N[0]
s = (a*(a+1))/2
for i in range(0, len(N)):
    s = s - N[i]
print(int(s + a))
