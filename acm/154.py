# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def zeros(n):
    res = 0
    while n:
        res += n
        n //= 5
    return res


def solve(n):
    if n == 0:
        return 1

    lo = 0
    hi = n
    while lo <= hi:
        mi = lo + hi >> 1
        z = zeros(mi)
        if z < n:
            lo = mi + 1
        elif z > n:
            hi = mi - 1
        else:
            return mi * 5
    return "No solution"


def main():
    print(solve(ir()))


if __name__ == "__main__":
    main()
