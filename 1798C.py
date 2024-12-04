# ruff: noqa: E741

from math import gcd, lcm
import sys

for _ in range(int(sys.stdin.readline())):
    ans = 0
    for i in range(int(sys.stdin.readline())):
        a, b = map(int, sys.stdin.readline().split())
        if i == 0:
            q = a
            p = b
            ans = 1
            continue
        l = lcm(b, p)
        mb = l // b
        mp = l // p
        if q % mp != 0 or a % mb != 0:
            q = a
            p = b
            ans += 1
        else:
            p = l
            q = gcd(q // mp, a // mb)
    print(ans)
