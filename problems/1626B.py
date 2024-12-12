# ruff: noqa: E731, E741
import sys

for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline().strip()
    d = list(map(int, n))
    i = next((i for i in reversed(range(len(d) - 1)) if d[i] + d[i + 1] >= 10), 0)
    print(n[:i] + str(d[i] + d[i + 1]) + n[i + 2 :])
