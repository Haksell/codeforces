# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n, m = mir()
    a = lmir()
    maxi = max(a)
    res = []
    for _ in range(m):
        c, l, r = read().split()
        if int(l) <= maxi <= int(r):
            maxi += 1 if c == "+" else -1
        res.append(maxi)
    print(*res)
