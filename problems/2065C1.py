# ruff: noqa: E731, E741
import math
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, _ = mir()
    a = lmir()
    b = lmir()
    prev = -math.inf
    for i in range(n):
        if a[i] < prev:
            a[i] = b[0] - a[i]
            if a[i] < prev:
                return False
        else:
            if prev <= b[0] - a[i] < a[i]:
                a[i] = b[0] - a[i]
        prev = a[i]
    return True


def main():
    for _ in rir():
        print("YES" if solve() else "NO")


if __name__ == "__main__":
    main()
