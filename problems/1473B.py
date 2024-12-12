# ruff: noqa: E731, E741
from math import gcd, lcm

for _ in range(int(input())):
    s = input()
    t = input()
    gcd_st = gcd(len(s), len(t))
    for i in range(gcd_st, min(len(s), len(t)) + 1, gcd_st):
        ss = s[:i]
        tt = t[:i]
        if (
            ss == tt
            and all(s[j : j + i] == ss for j in range(i, len(s), i))
            and all(t[j : j + i] == tt for j in range(i, len(t), i))
        ):
            lcm_st = lcm(len(s), len(t))
            print(lcm_st // i * ss)
            break
    else:
        print(-1)
