# ruff: noqa: E731, E741
import sys


def solve(n, a, b):
    if a == 1:
        return (n - 1) % b == 0
    i = 1
    while i <= n:
        if (n - i) % b == 0:
            return True
        i *= a
    return False


for _ in range(int(sys.stdin.readline())):
    n, a, b = map(int, sys.stdin.readline().split())
    print("YES" if solve(n, a, b) else "NO")
