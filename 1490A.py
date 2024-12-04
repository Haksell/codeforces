from math import *
import sys
read = sys.stdin.readline
write = lambda x, end="\n": sys.stdout.write(x + end)

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    z = 0
    for i in range(n - 1):
        a, b = sorted(l[i:i + 2])
        x = max(0, ceil(log2(b / a)) - 1)
        z += x
        #print(i, x)
    print(z)