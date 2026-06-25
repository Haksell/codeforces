# ruff: noqa: E731, E741
from itertools import combinations
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def score(i, j, k):
    return (i ^ j) + (j ^ k) + (k ^ i)


def naive(l, r):
    m = max(score(i, j, k) for i, j, k in combinations(range(l, r + 1), r=3))
    return next(
        (i, j, k)
        for i, j, k in combinations(range(l, r + 1), r=3)
        if score(i, j, k) == m
    )


def smart(l, r):
    b = 1 << (r.bit_length() - 1)
    if b - 2 >= l:
        return (b - 2, b - 1, b)
    elif b - 1 == l:
        return (b - 1, b, b + 1)
    else:
        i, j, k = smart(l - b, r - b)
        return (i | b, j | b, k | b)


def main():
    for _ in rir():
        l, r = mir()
        print(*smart(l, r))


def test():
    for l in range(100):
        for r in range(l + 2, 100):
            rn = naive(l, r)
            rs = smart(l, r)
            if (
                len(rs) != 3
                or len(set(rs)) != 3
                or min(rs) < l
                or max(rs) > r
                or score(*rn) != score(*rs)
            ):
                print(l, r, "!", rn, score(*rn), rs, score(*rs))
                return


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
