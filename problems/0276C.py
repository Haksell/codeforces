# ruff: noqa: E731, E741
from itertools import accumulate
import sys

n, q = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
start = [0] * n
end = [0] * (n + 1)
for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    start[x - 1] += 1
    end[y] += 1
acc = list(accumulate(s - e for s, e in zip(start, end)))
print(sum(x * y for x, y in zip(sorted(a), sorted(acc))))
