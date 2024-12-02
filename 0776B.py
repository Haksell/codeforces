# ruff: noqa: E731, E741
from math import isqrt
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    if n <= 2:
        print(1)
        print(*[1] * n)
        return
    n += 2
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    print(2)
    print(*[1 + b for b in sieve[2:]])


if __name__ == "__main__":
    main()
