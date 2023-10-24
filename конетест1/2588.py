import numpy as np
N = list(map(int, input().split()))
m = N[0]
n = N[1]
count = 0
bip = -1
while m % 2 == 1 and n % 2 == 1:
    m = (m-1)/2
    n = (n-1)/2
    bip += 1
    count += 4**bip
print(count)
