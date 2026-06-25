# ruff: noqa: E731, E741
from bisect import bisect_left, bisect_right
from functools import reduce
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

MOD = 998244353


def solve():
    _, q = mir()
    a = lmir()
    b = lmir()
    sa = sorted(a)
    sb = sorted(b)
    c = reduce(lambda acc, pair: acc * min(pair) % MOD, zip(sa, sb), initial=1)
    res = [c]
    for _ in range(q):
        op, i = mir()
        i -= 1
        arr, sorted_arr = (a, sa) if op == 1 else (b, sb)
        lo = bisect_left(sorted_arr, arr[i])
        hi = bisect_right(sorted_arr, arr[i])
        old_lo = min(sa[lo], sb[lo])
        old_hi = min(sa[hi - 1], sb[hi - 1])
        arr[i] += 1
        sorted_arr[lo] += 1
        if lo != hi - 1:
            sorted_arr[lo], sorted_arr[hi - 1] = sorted_arr[hi - 1], sorted_arr[lo]
        new_lo = min(sa[lo], sb[lo])
        if old_lo != new_lo:
            c *= new_lo
            c *= pow(old_lo, -1, MOD)
        if lo != hi - 1:
            new_hi = min(sa[hi - 1], sb[hi - 1])
            if old_hi != new_hi:
                c *= new_hi
                c *= pow(old_hi, -1, MOD)
        c %= MOD
        res.append(c)
    print(*res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
