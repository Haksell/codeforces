# ruff: noqa: E731, E741
from functools import cache
import sys

sys.setrecursionlimit(10000)


@cache
def dfs(i):
    return 1 if tree[i] is None else 1 + dfs(tree[i])


n = int(input())
tree = [None] * n
for i in range(n):
    m = int(input()) - 1
    if m >= 0:
        tree[i] = m
print(max(map(dfs, range(n))))
