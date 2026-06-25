# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def int_ceil(n, k):
    return (n + k - 1) // k


for _ in rir():
    n = ir()
    x, y = mir()
    print(int_ceil(n, min(x, y)))
