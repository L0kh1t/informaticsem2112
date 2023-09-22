N = list(map(int, input().split()))
a = N[0]
b = N[1]
def f(a, b):
    m = 0
    if a > b:
        m = a
    if b > a:
        m = b
    while(True):
        if (m % a == 0) and (m % b == 0):
            d = m
            break
        m += 1
    return d
result = str(f(a, b)//a) + ' ' + str(f(a, b)//b) + ' ' + str(f(a, b))
print(result)
