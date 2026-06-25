# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
rir = lambda: range(int(read()))
ir = lambda: int(read())
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    a = list(range(1, n + 1))
    print(n)
    print(*a)
    for i in range(n - 1):
        a[i], a[i + 1] = a[i + 1], a[i]
        print(*a)
