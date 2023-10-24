f = open('input.txt', 'r')
line = f.readlines()
n = line[0]
p = list(map(int, line[1].split()))
b = 0
while len(p) > 0:
    b += p[p.index(max(p))]*p.index(max(p)) - sum(p[0:p.index(max(p))])
    p = p[p.index(max(p))+1:]
print(b)
