# ruff: noqa: E731, E741
from random import randint, randrange
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: list(map(int, read().split()))
lmir = lambda: list(map(int, read().split()))


def naive(p, a):
    remain = set(range(p)) - set(a)
    if not remain:
        return 0
    d0 = a[-1]
    res = 0
    for n in [*range(d0 + 1, p), 0]:
        remain.discard(n)
        res += 1
        if not remain:
            return res
    for i in range(len(a) - 2, -1, -1):
        if a[i] != p - 1:
            d = a[i]
            break
    else:
        d = 0
    d += 1
    remain.discard(d)
    if not remain:
        return res
    for n in range(1, d0):
        remain.discard(n)
        res += 1
        if not remain:
            return res


def smart(p, a):
    s = set(a)
    if p <= 100 and s == set(range(p)):
        return 0
    d0 = a[-1]
    smaller = [n for n in range(d0 - 1, max(d0 - 103, -1), -1) if n not in s]
    if not smaller:
        return next(n for n in range(p - 1, -1, -1) if n not in s) - d0
    d1 = next((d1 for d1 in a[:-1][::-1] if d1 != p - 1), 0) + 1
    if d1 in smaller:
        smaller.remove(d1)
    if not smaller:
        return p - d0
    bs = max(smaller)
    if bs == 0:
        return p - d0
    return (bs - d0) % p


def test(p, a):
    n = naive(p, a)
    s = smart(p, a)
    assert n == s, f"{p=} {a=} {naive(p,a)=} {smart(p,a)=}"


for _ in range(1000):
    n = randint(1, 10)
    p = randint(2, 100)
    a = [randrange(1 if i == 0 else 0, p) for i in range(n)]
    test(p, a)

for _ in rir():
    _, p = mir()
    a = lmir()
    print(smart(p, a))
