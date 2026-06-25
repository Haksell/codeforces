# ruff: noqa: E731, E741
import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    print("YES" if a[0] < a[-1] else "NO")
