# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: list(map(int, read().split()))
lmir = lambda: list(map(int, read().split()))


def f(n):
    res = 0
    while n % 10 == 0:
        res += 1
        n //= 10
    return res


def naive(old, mul):
    return max([n * old for n in range(1, mul + 1)], key=lambda n: (f(n), n))


def smart(old, mul):
    two = five = 0
    n = old
    while n & 1 == 0:
        n >>= 1
        two += 1
    while n % 5 == 0:
        n //= 5
        five += 1
    res = 1
    while two < five and 2 * res <= mul:
        two += 1
        res *= 2
    while two > five and 5 * res <= mul:
        five += 1
        res *= 5
    while 10 * res <= mul:
        res *= 10
    res = mul // res * res
    return res * old


for _ in rir():
    old, mul = mir()
    print(smart(old, mul))
