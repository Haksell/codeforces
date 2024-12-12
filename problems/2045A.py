# ruff: noqa: E731, E741
from collections import Counter
from functools import cache
from itertools import product
import math
import sys

sys.setrecursionlimit(30000)
read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


@cache
def naive(y, ng, vow, cons):
    if y < 0 or ng < 0 or vow < 0 or cons < 0:
        return -math.inf
    return max(
        3 + naive(y - 2, ng, vow - 1, cons),
        5 + naive(y, ng - 2, vow - 1, cons - 4),
        3 + naive(y, ng, vow - 1, cons - 2),
        4 + naive(y - 1, ng - 1, vow - 1, cons - 2),
        3 + naive(y - 1, ng, vow - 1, cons - 1),
        4 + naive(y, ng - 1, vow - 1, cons - 3),
        3 + naive(y - 3, ng, vow, cons),
        4 + naive(y - 2, ng - 1, vow, cons - 2),
        3 + naive(y - 2, ng, vow, cons - 1),
        5 + naive(y - 1, ng - 2, vow, cons - 4),
        3 + naive(y - 1, ng, vow, cons - 2),
        4 + naive(y - 1, ng - 1, vow, cons - 3),
        0,
    )


@cache
def smart_naive(y, vow, cons):
    if y < 0 or vow < 0 or cons < 0:
        return -math.inf
    return max(
        3 + smart_naive(y - 2, vow - 1, cons),
        3 + smart_naive(y, vow - 1, cons - 2),
        3 + smart_naive(y - 1, vow - 1, cons - 1),
        3 + smart_naive(y - 3, vow, cons),
        3 + smart_naive(y - 2, vow, cons - 1),
        3 + smart_naive(y - 1, vow, cons - 2),
        0,
    )


@cache
def nong(y, vow, cons):
    if y < 0 or vow < 0 or cons < 0:
        return -math.inf
    sy = min(vow, cons // 2)
    vow -= sy
    cons -= 2 * sy
    # print(sy, vow, cons, y)
    if vow == 0:
        return 3 * (sy + min((y + cons) // 3, y))
    if cons and y >= 1 and vow >= 1:
        cons -= 1
        y -= 1
        vow -= 1
        sy += 1
    sy2 = min(vow, y // 2)
    vow -= sy2
    y -= 2 * sy2
    sy += sy2
    return 3 * sy + smart_naive(y, vow, cons)


@cache
def smart(y, ng, vow, cons):
    res = 0
    taken = 0
    while ng >= 0:
        res = max(res, 5 * taken + nong(y, vow, cons))
        if ng:
            res = max(
                res,
                5 * taken + 4 + nong(y, vow - 1, cons - 3),
                5 * taken + 4 + nong(y - 1, vow, cons - 3),
                5 * taken + 4 + nong(y - 1, vow - 1, cons - 2),
                5 * taken + 4 + nong(y - 2, vow, cons - 2),
            )
        if vow >= 1:
            vow -= 1
        elif y >= 1:
            y -= 1
        else:
            break
        ng -= 2
        cons -= 4
        taken += 1
    return res


def parse():
    VOWELS = "AEIOU"
    s = input()
    c = Counter(s)
    y = c["Y"]
    ng = min(c["N"], c["G"])
    vow = sum(v for k, v in c.items() if k in VOWELS)
    cons = sum(v for k, v in c.items() if k not in VOWELS and k != "Y")
    return y, ng, vow, cons


def main():
    y, ng, vow, cons = parse()
    print(smart(y, ng, vow, cons))


def test():
    for y, n, v, c in product(range(30), repeat=4):
        if 2 * n > c:
            continue
        rn = naive(y, n, v, c)
        rs = smart(y, n, v, c)
        if rn != rs:
            print(f"{y=} {n=} {v=} {c=}", "|", rn, rs)
            return


if __name__ == "__main__":
    main()
