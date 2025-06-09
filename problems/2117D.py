# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

"""
-i
+i-n-1

-1 -5
-2 -4
-3 -3
-4 -2
-5 -1

21 18 15 12 9
16 14 12 10 8
11 10 9 8 7
6 6 6 6 6
5 4 3 2 1
0 0 0 0 0
"""


def solve(n, a):
    d = a[0] - a[1]
    if any(x - y != d for x, y in zip(a[1:], a[2:])):
        return False
    eq = min(a[0], a[-1]) - abs(d)
    return eq >= 0 and eq % (n + 1) == 0


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        print("YES" if solve(n, a) else "NO")


if __name__ == "__main__":
    main()
