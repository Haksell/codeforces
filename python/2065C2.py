# ruff: noqa: E731, E741
from bisect import bisect_left
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, m = mir()
    a = lmir()
    b = sorted(lmir())

    mb = min(b)
    if mb - a[0] < a[0]:
        a[0] = mb - a[0]

    for i in range(1, n):
        prev = a[i - 1]
        j = bisect_left(b, prev + a[i])
        if a[i] < prev:
            if j == m:
                return False
            a[i] = b[j] - a[i]
        else:
            if j < m and prev <= b[j] - a[i] < a[i]:
                a[i] = b[j] - a[i]
        prev = a[i]
    return True


def main():
    for _ in rir():
        print("YES" if solve() else "NO")


if __name__ == "__main__":
    main()
