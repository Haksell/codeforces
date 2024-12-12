# ruff: noqa: E731, E741
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = sorted(map(int, sys.stdin.readline().split()))
    blue = sum(a[: (n + 1) >> 1])
    red = sum(a[(n >> 1) + 1 :])
    print("YES" if red > blue else "NO")
