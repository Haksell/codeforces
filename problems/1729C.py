# ruff: noqa: E731, E741
import sys

sys.setrecursionlimit(25000)
read = sys.stdin.readline
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    s = read().strip()
    first = s[0]
    last = s[-1]
    between = [
        i for i, c in enumerate(s[1:-1], 2) if first <= c <= last or last <= c <= first
    ]
    between.sort(key=lambda i: s[i - 1])
    if last < first:
        between.reverse()
    l = [1] + between + [len(s)]
    print(abs(ord(first) - ord(last)), len(l))
    print(*l)
