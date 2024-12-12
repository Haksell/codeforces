# ruff: noqa: E731, E741
import sys


def is_sorted(a):
    return all(x <= y for x, y in zip(a, a[1:]))


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    evens = [ai for ai in a if ai & 1 == 0]
    odds = [ai for ai in a if ai & 1 == 1]
    print("YES" if is_sorted(evens) and is_sorted(odds) else "NO")
