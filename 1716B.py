# ruff: noqa: E731
import sys

cin = sys.stdin
read = cin.readline
cout = sys.stdout
write = cout.write
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
