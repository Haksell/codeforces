# ruff: noqa: E731, E741
from math import gcd
import re
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


PALINDROMES = {
    0,
    70,
    140,
    210,
    280,
    350,
    601,
    671,
    741,
    811,
    881,
    951,
    1202,
    1272,
    1342,
    1412,
}


def main():
    for _ in rir():
        h, m, x = map(int, re.findall(r"\d+", input()))
        if gcd(x, 1440) == 1:
            print(len(PALINDROMES))
            continue
        t = t0 = 60 * h + m
        r = 0
        while True:
            r += t in PALINDROMES
            t = (t + x) % 1440
            if t == t0:
                break
        print(r)


if __name__ == "__main__":
    main()
