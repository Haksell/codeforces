# ruff: noqa: E731, E741
import sys

lines = [list(map(int, line.split())) for line in sys.stdin]
for i in range(lines[0][0]):
    n, x = lines[4 * i + 1]
    a = sorted(lines[4 * i + 2])
    b = sorted(lines[4 * i + 3], reverse=True)
    print("YES" if all(ai + bi <= x for ai, bi in zip(a, b)) else "NO")
