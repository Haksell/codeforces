# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, k = mir()
    hi = n
    mul = 0
    i = 0
    while hi >= k:
        mi = hi + 1 >> 1
        if hi & 1:
            mul |= 1 << i
            mi -= 1
        hi = mi
        i += 1
    print((n + 1) * mul >> 1)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
