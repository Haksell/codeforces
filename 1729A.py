# ruff: noqa: E731, E741
import sys

sys.setrecursionlimit(25000)
cin = sys.stdin
read = cin.readline
cout = sys.stdout
write = cout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    a, b, c = mir()
    y = abs(b - c) + c
    print(1 if a < y else 2 if a > y else 3)
