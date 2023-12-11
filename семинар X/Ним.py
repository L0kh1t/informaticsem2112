N = list(map(int, input().split()))
A = N.copy()


def change(x, y):
    for i in range(len(y)):
        if x[len(x) - 1 - y[len(y) - i-1]] == '0':
            x = str(int(x) + 10**y[len(y) -1- i])
        elif x[len(x) - 1 - y[len(y) - i-1]] == '1':
            x = str(int(x) - 10 ** y[len(y) - i -1 ])


def vbin(N):
    c = 0
    for i in range(0, len(N)):
        N[i] = str(format(N[i], 'b'))
        if len(N[i]) > c:
            print(len(N[i]))
            c = len(N[i])
    print(N)
    print(max(N), c)
    dic = {}
    for j in range(0, c):
        count = 0
        for i in range(0, len(N)):
            if len(N[i]) - 1 < j:
                continue
            else:
                count += int(N[i][j])
        dic[c - j - 1] = count
    return dic, c


D = vbin(N)[0]
flag = True
print(D)
print(D[0])
for i in range(len(D)):
    if D[i] % 2 != 0:
        print('Ходи первым')
        flag = False
        break
if flag == True:
    print('Ходи вторым')
    N = list(map(int, input().split()))
else:
    N = A

while N != [0]:
    D, c = vbin(N)
    print(D, '!')
    M = []
    for i in range(len(D)):
        if D[i] % 2 != 0:
            M += [i]
    print(M)
    for i in range(0, len(N)):
        if len(N[i]) - 1 >= M[-1]:
            print(N[i], 'SUCK MY DICK')
            if int(N[i][len(N[i]) - M[-1] - 1]) == 1:
                change(N[i], M)
                print(N[i], )
                break
    print(N)
