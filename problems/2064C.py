# ruff: noqa: E731, E741
from random import choices, randint, seed
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def naive(a):
    if len(a) == 0:
        return 0
    res = 0
    for i, ai in enumerate(a):
        if ai > 0:
            res = max(res, ai + naive(a[i + 1 :]))
        else:
            res = max(res, -ai + naive(a[:i]))
    return res


def smart(a):
    pos = [0]
    for ai in a:
        if ai > 0:
            pos.append(pos[-1] + ai)
        else:
            pos.append(pos[-1])
    neg = [0]
    for ai in reversed(a):
        if ai < 0:
            neg.append(neg[-1] - ai)
        else:
            neg.append(neg[-1])
    neg.reverse()
    return max(map(sum, zip(pos, neg)))


def solve():
    read()
    a = lmir()
    print(smart(a))


def main():
    for _ in rir():
        solve()


def test():
    seed(0)
    ch = list(range(-20, 21))
    ch.remove(0)
    for _ in range(1000):
        n = randint(1, 12)
        a = choices(ch, k=n)
        rn = naive(a)
        rs = smart(a)
        if rn != rs:
            print(_, a, rn, rs)
            return


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
