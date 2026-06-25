# ruff: noqa: E731, E741
from collections import Counter
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

LIM = 1_000_001
BIGGEST_FACTOR = list(range(LIM))
for i in range(2, LIM):
    if BIGGEST_FACTOR[i] == i:
        for j in range(i * i, LIM, i):
            BIGGEST_FACTOR[j] = i


def get_factors(n):
    factors = Counter()
    while n > 1:
        factor = BIGGEST_FACTOR[n]
        factors[factor] += 1
        n //= factor
    return factors


def solve():
    n = ir()
    a = lmir()
    factors = Counter()
    for ai in a:
        factors += get_factors(ai)
    print("YES" if all(v % n == 0 for v in factors.values()) else "NO")


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
