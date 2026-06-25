# ruff: noqa: E731, E741
import sys
from functools import reduce
from operator import xor

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


MOD = 998244353


def solve(n, x):
    if n <= 2:
        return 0
    if n & 1 == 1:
        return solve(n + 1, x)
    if n == x:
        return 0
    if n == x + 1:
        return solve(n, n - 2)
    if 2 * x > n:
        return solve(n, n - x - 1)

    x = x // 2 + 1
    if n & 3 == 0:
        res = n // 4 * x - x * (x - 1) // 2
        return res % MOD
    else:
        res = n // 4 * x
        res += x
        res -= x * (x - 1) // 2
        res -= (x + 3) // 2 - 1
        return res % MOD


def naive(n, x):
    res = 0
    for i in range(1, x + 1):
        for j in range(x, n + 1):
            p = reduce(xor, range(i, j + 1))
            res += p == 0
    return res


def main():
    for _ in rir():
        n, x = mir()
        print(solve(n, x))


def test():
    for n in range(2, 100, 1):
        for x in range(1, n + 1):
            rn = naive(n, x)
            rs = solve(n, x)
            print(n, x, ":", rn, rs, "NO" if rn != rs else "")
            assert rs == rn, (n, x, rn, rs)
        print()


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()