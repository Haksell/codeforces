# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    a = lmir()
    print(sum(a) - 2 * a[-2])
