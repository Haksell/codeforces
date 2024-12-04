from heapq import *
from itertools import *
import sys
read = sys.stdin.readline
write = lambda x, end="\n": sys.stdout.write(x + end)

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = sorted(l)
    c = list(accumulate(s))
    z = 1
    #print(s, c)
    for i in range(n - 1):
        if c[i] >= s[i + 1]:
            z += 1
        else:
            z = 1
    x = nlargest(z, [(n, i) for i, n in enumerate(l)])
    print(z)
    print(*sorted(i + 1 for _, i in x))


"""
1
4
1 1 1 4
"""