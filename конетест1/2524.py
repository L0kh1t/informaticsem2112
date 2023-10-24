f = open('input.txt', 'r')
line = f.readlines()
t = int(line[0])

a = 'a'
b = 'b'

for j in range(1, t+1):
    N = list(map(int, line[j].split()))
    m = [a, b] + ['0'] * (N[0] - 1)
    for i in range(2, N[0] + 1):
        m[i] = (m[i - 2] + m[i - 1])
    print(m[N[0]][N[1] - 1])
