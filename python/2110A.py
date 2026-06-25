# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n = ir()
    a = sorted(mir())
    s = (a[0] + a[-1]) & 1
    if s == 0:
        return 0
    else:
        lo = next(i for i in range(n) if a[i] & 1 != a[0] & 1)
        hi = next(i for i in reversed(range(n)) if a[i] & 1 != a[-1] & 1)
        return min(lo, n - hi - 1)


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
