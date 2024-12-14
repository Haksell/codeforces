# ruff: noqa: E731, E741
from operator import or_, xor
import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
steps = [a]
for i in range(n):
    op = xor if i & 1 else or_
    steps.append([op(x, y) for x, y in zip(steps[-1][0::2], steps[-1][1::2])])
ans = []
for line in sys.stdin:
    p, b = map(int, line.split())
    p -= 1
    steps[0][p] = b
    for i in range(n):
        op = xor if i & 1 else or_
        steps[i + 1][p >> 1] = op(steps[i][p], steps[i][p ^ 1])
        p >>= 1
    ans.append(str(steps[-1][0]))
sys.stdout.write("\n".join(ans))
