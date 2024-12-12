# ruff: noqa: E731, E741
from math import gcd
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


LIM = 10_000_001


def smart(smallest_factors, x, y):
    diff = y - x
    if diff == 1:
        return -1
    if gcd(x, y) != 1:
        return 0
    ans = 1 << 25
    while diff != 1:
        f = smallest_factors[diff]
        if x % f == y % f:
            m = -x % f
            ans = min(ans, m)
        diff //= f
    return ans


def main():
    smallest_factors = list(range(LIM))
    for i in range(2, LIM):
        if i == smallest_factors[i]:
            for j in range(i + i, LIM, i):
                smallest_factors[j] = i
    for _ in rir():
        x, y = mir()
        print(smart(smallest_factors, x, y))


if __name__ == "__main__":
    main()
