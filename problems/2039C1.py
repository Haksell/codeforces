# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def naive(x, m):
    return sum(
        x != y and (x % (x ^ y) == 0 or y % (x ^ y) == 0) for y in range(1, m + 1)
    )


def smart(x, m):
    res = 0
    for y in range(1, min(2 * x, m) + 1):
        d = x ^ y
        if x != y and (y % d == 0 or x % d == 0):
            res += 1
    return res


def main():
    MODE = 2
    if MODE == 0:
        for x in range(1, 101):
            for y in range(1, 301):
                if x != y and (x % (x ^ y) == 0 or y % (x ^ y) == 0):
                    print(
                        x, y, x ^ y, x != y and (x % (x ^ y) == 0 or y % (x ^ y) == 0)
                    )
            print()
    elif MODE == 1:
        for x in range(1, 11):
            for m in range(1, 11):
                n = naive(x, m)
                s = smart(x, m)
                assert n == s, (x, m, n, s)
    else:
        for _ in rir():
            x, m = mir()
            print(smart(x, m))


if __name__ == "__main__":
    main()
