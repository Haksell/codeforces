# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: list(map(int, read().split()))
lmir = lambda: list(map(int, read().split()))


def bgg(h, a):
    res = 0
    l = 0
    for p in a:
        if p >= h and l == 0:
            h *= 3
            l += 1
        if p >= h and l == 1:
            h *= 2
            l += 1
        if p >= h and l == 2:
            h *= 2
            l += 1
        if p >= h and l == 3:
            break
        res += 1
        h += p // 2
    return res


def gbg(h, a):
    res = 0
    l = 0
    for p in a:
        if p >= h and l == 0:
            h *= 2
            l += 1
        if p >= h and l == 1:
            h *= 3
            l += 1
        if p >= h and l == 2:
            h *= 2
            l += 1
        if p >= h and l == 3:
            break
        res += 1
        h += p // 2
    return res


def ggb(h, a):
    res = 0
    l = 0
    for p in a:
        if p >= h and l == 0:
            h *= 2
            l += 1
        if p >= h and l == 1:
            h *= 2
            l += 1
        if p >= h and l == 2:
            h *= 3
            l += 1
        if p >= h and l == 3:
            break
        res += 1
        h += p // 2
    return res


for _ in rir():
    _, h = mir()
    a = sorted(mir())
    print(
        max(
            bgg(h, a),
            gbg(h, a),
            ggb(h, a),
        )
    )
