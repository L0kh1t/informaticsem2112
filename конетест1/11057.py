N = list(map(int, input().split()))
a = N[0]
b = N[1]
x = 0
c = a
d = b
while c % b != 0 or d % a != 0:
    c += 1
    d += 1
print(c - a)
