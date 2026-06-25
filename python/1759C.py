# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: list(map(int, read().split()))
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    l, r, x = mir()
    a, b = sorted(mir())
    if a == b:
        print(0)
    elif (a + x > r and a - x < l) or (b + x > r and b - x < l):
        print(-1)
    elif abs(a - b) < x:
        print(3 if a - x < l and b + x > r else 2)
    else:
        print(1)
