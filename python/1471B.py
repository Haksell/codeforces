# ruff: noqa: E731, E741
import sys


def repeats(numer, denom):
    ans = 0
    while numer % denom == 0:
        ans += 1
        numer //= denom
    return ans


for _ in range(int(sys.stdin.readline())):
    _, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    r = [repeats(ai, x) for ai in a]
    minr = min(r)
    mini = next(i for i, ri in enumerate(r) if ri == minr)
    ans = 0
    for i, (ai, ri) in enumerate(zip(a, r)):
        count = min(ri, minr + 1) if i < mini else min(ri, minr)
        ans += ai * (count + 1)
    print(ans)
