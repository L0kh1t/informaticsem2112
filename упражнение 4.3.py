N = list(map(str, input().split()))
symb = N[1]
c = 1
size = int(N[0])
while c <= size:
    print(symb*c)
    c += 1
if c > size:
    while c > 0:
        c -= 1
        print(symb*c)
