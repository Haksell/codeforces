# ruff: noqa: E731, E741
from heapq import nlargest
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, k = mir()
    t = [[] for _ in range(n)]
    for _ in range(n - 1):
        i, j = mir()
        t[i - 1].append(j - 1)
        t[j - 1].append(i - 1)
    parents = [-1] * n
    depths = [0] * n
    q = [0]
    for i in q:
        for j in t[i]:
            t[j].remove(i)
            parents[j] = i
            depths[j] = depths[i] + 1
        q += t[i]
    sizes = [0] * n
    for i in q[:0:-1]:
        sizes[parents[i]] += sizes[i] + 1
    scores = list(map(int.__sub__, depths, sizes))
    print(sum(nlargest(k, scores)))


if __name__ == "__main__":
    main()
