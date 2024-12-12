# ruff: noqa: E731, E741
from heapq import nlargest
import sys

ans = []
for _ in range(int(sys.stdin.readline())):
    _, h = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    x, y = nlargest(2, a)
    z = x + y
    q, r = divmod(h, z)
    ans.append(2 * q + (r > 0) + (r > x))
sys.stdout.write("\n".join(map(str, ans)))
