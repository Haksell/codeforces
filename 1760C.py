# ruff: noqa: E731, E741
from heapq import nlargest
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    n = ir()
    s = lmir()
    a, b = nlargest(2, s)
    print(*[x - b if x == a else x - a for x in s])
