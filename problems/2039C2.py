# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def naive(x, m):
    return sum((x ^ y) % x == 0 or (x ^ y) % y == 0 for y in range(1, m + 1))


def smart(x, m):
    if x == 1:
        return m
    res = 0
    lim = 1 << x.bit_length()
    for y in range(1, min(lim, m + 1)):
        d = x ^ y
        if d % y == 0 or d % x == 0:
            res += 1
    if lim > m:
        return res
    res += m // x
    res -= (lim - 1) // x
    for nx in range(-2, 3):
        nxt = m // x * x + nx * x
        y = x ^ nxt
        if y == 0:
            continue
        if y <= m and nxt > m:
            res += 1
        if nxt <= m and y > m:
            res -= 1
    return res


def main():
    MODE = 2
    if MODE == 0:
        for x in range(1, 51):
            for y in range(1, 251):
                xy = x ^ y
                if x != y and xy % x == 0 or xy % y == 0:
                    print(x, y, xy, xy % x, xy % y)
            print()
    elif MODE == 1:
        for x in range(1, 101):
            for m in range(1, 501):
                n = naive(x, m)
                s = smart(x, m)
                assert n == s, (x, m, n, s)
    else:
        for _ in rir():
            x, m = mir()
            print(smart(x, m))


if __name__ == "__main__":
    main()
