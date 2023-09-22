N = list(map(int, input().split()))
a = N[0]
b = N[1]
m = a
n = b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print(str(a+b)+" " + str((m/(a+b))) + " " + str(n/(a+b)))
