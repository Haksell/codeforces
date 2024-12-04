from itertools import *
from collections import *
import sys
read = sys.stdin.readline
write = lambda x, end="\n": sys.stdout.write(x + end)

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = Counter(Counter(l).values())
    res = n
    last = 1 << 28
    count = 0
    tot = 0
    x = 0
    # print(s)
    #print(n, sum(k * v for k, v in s.items()))
    for k, v in sorted(s.items(), reverse=True):
        # print(tot)
        tot += (last - k) * count
        cand = tot + (n - x - k * v)
        #print(k, v, tot, cand)
        #print(tot, cand)
        res = min(res, cand)
        last = k
        count += v
        x += k * v
    #print(n, count)
    print(res)
    # print()