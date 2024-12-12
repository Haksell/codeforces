# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline

n, q, k = map(int, input().split())
a = list(map(int, input().split()))
for line in sys.stdin:
    lo, hi = [int(n) - 1 for n in line.split()]
    if lo == hi:
        print(k - 1)
        continue
    z = k + a[hi] - a[lo] - 1 - 2 * (hi - lo)
    print(z)
