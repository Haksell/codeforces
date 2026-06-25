# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n = ir() + 1
    a = lmir()

    cnt = [0] * n
    for ai in a:
        cnt[ai] += 1

    factors = [0] * n
    for i in range(2, n):
        if factors[i] == 0:
            for j in range(i, n, i):
                factors[j] += 1
                jj = j // i
                while jj % i == 0:
                    factors[j] += 1
                    jj //= i

    primes = 0
    res = 0
    for i in range(2, n):
        if cnt[i] == 0 or factors[i] >= 3:
            continue
        if factors[i] == 2:
            res += cnt[i] * (cnt[i] + 1) >> 1
            continue
        res += cnt[i] * primes
        for j in range(2 * i, n, i):
            if factors[j] == 2:
                res += cnt[i] * cnt[j]
        primes += cnt[i]

    return res


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
