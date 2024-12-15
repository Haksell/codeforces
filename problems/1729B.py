# ruff: noqa: E731, E741
import sys

sys.setrecursionlimit(25000)
read = sys.stdin.readline
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    t = list(map(int, read().strip()))
    s = []
    cur = 0
    i = n - 1
    while i >= 0:
        if t[i] == 0:
            x = 10 * t[i - 2] + t[i - 1]
            i -= 3
        else:
            x = t[i]
            i -= 1
        s.append(chr(x + 96))
    print("".join(s[::-1]))
