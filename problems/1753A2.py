# ruff: noqa: E731, E741
from functools import reduce
from operator import xor
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        if reduce(xor, a) & 1:
            print(-1)
            continue
        res = []
        lo = 0
        while True:
            # skip zeros
            hi = lo
            while hi < n and a[hi] == 0:
                hi += 1
            if lo != hi:
                res.append((lo, hi - 1))
            if hi == n:
                break
            # build pairs
            lo = hi
            hi += 1
            parity = -1
            while a[hi] == 0:
                parity *= -1
                hi += 1
            if a[lo] + a[hi] * parity == 0:
                res.append((lo, hi))
            elif parity == -1:
                res.append((lo, hi - 1))
                res.append((hi, hi))
            else:
                res.append((lo, hi - 2))
                res.append((hi - 1, hi))
            lo = hi + 1
        print(len(res))
        for l, r in res:
            print(l + 1, r + 1)


if __name__ == "__main__":
    main()
