# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n, k = mir()
    factors = dict()
    d = 2
    while d * d <= n:
        cnt = 0
        while n % d == 0:
            n //= d
            cnt += 1
        if cnt:
            factors[d] = cnt
        d += 1
    if n > 1:
        factors[n] = 1
    divisors = [1]
    for p, v in factors.items():
        divisors = [d * p**i for d in divisors for i in range(v + 1)]
    divisors.sort()
    print(-1 if k > len(divisors) else divisors[k - 1])


if __name__ == "__main__":
    main()
