# ruff: noqa: E731, E741
import sys


def f(s):
    res = dots = 0
    for c in s:
        if c == ".":
            dots += 1
        else:
            res += dots
    return res


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    sheep = [i for i, c in enumerate(s) if c == "*"]
    if not sheep:
        print(0)
        continue
    m = sheep[len(sheep) >> 1]
    print(f(s[m + 1 :]) + f(s[max(0, m - 1) :: -1]))
