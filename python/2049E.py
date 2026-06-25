# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def q(l, r):
    print("?", l, r, flush=True)
    return input() == "1"


def bisect_start(lo, hi, expected):
    while lo + 1 < hi:
        mi = (lo + hi - 1) >> 1
        if q(1, mi) == expected:
            lo = mi + 1
        else:
            hi = mi + 1
    return lo


def bisect_end(lo, hi, expected, n):
    while lo + 1 < hi:
        mi = (lo + hi - 1) >> 1
        l = n - mi + 1
        if q(l, n) == expected:
            lo = mi + 1
        else:
            hi = mi + 1
    return lo


def solve_big(n, quarter):
    lo = n // 4 + 1
    mi = n // 2 + 1
    if q(1, n // 2):
        if quarter <= 1:
            return bisect_start(mi, n, True)
        else:
            return bisect_start(lo, mi, False)
    else:
        if quarter <= 1:
            return bisect_end(lo, mi, False, n)
        else:
            return bisect_end(mi, n, True, n)


def solve_small(n, quarter):
    lo = 2
    hi = n // 4 + 1
    return bisect_end(lo, hi, False, n) if quarter == 0 else bisect_start(lo, hi, False)


def solve_4(quarter):
    start = 1 if quarter == 0 else quarter
    end = start + 1
    return 3 if q(start, end) else 2


def solve(n):
    q0 = q(1, n // 4)
    q1 = q(n // 4 + 1, n // 2)
    q2 = q(n // 2 + 1, 3 * n // 4)
    quarter = 3 if q0 == q1 == q2 else 2 if q0 == q1 else 1 if q0 == q2 else 0
    if n == 4:
        return solve_4(quarter)
    elif q0 + q1 + q2 <= 1:
        return solve_big(n, quarter)
    else:
        return solve_small(n, quarter)


def main():
    for _ in rir():
        print("!", solve(ir()), flush=True)


if __name__ == "__main__":
    main()
