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
    a, b = mir()
    if a & 1:
        print("NO")
    elif a == 0:
        print("YES" if b & 1 == 0 else "NO")
    else:
        print("YES")
