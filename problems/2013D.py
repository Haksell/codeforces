# ruff: noqa: E731, E741
from itertools import accumulate
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
    if n == 1:
        print(0)
        continue
    mini = min(n // i for i, n in enumerate(accumulate(a), 1))
    maxi = max((n + i - 1) // i for i, n in enumerate(accumulate(reversed(a)), 1))
    print(maxi - mini)
