import sys


def f(a, b):
    best = (sys.maxsize, -1)
    for x in range(max(a, b) + 1):
        val = abs((a ^ x) - (b ^ x))
        best = min(best, (val, x))
    return best


def naive(a, b, r):
    res = (sys.maxsize, 0)
    for x in range(r + 1):
        pair = (abs((a ^ x) - (b ^ x)), x)
        res = min(res, pair)
    return res


def smart(a, b, r):
    if r == 0:
        return (abs(a - b), 0)
    mask = (1 << r.bit_length() - 1) - 1
    if r == mask:
        c = abs(a - b)
    else:
        c = smart(a, b, mask)[0]
    x = 0
    for i in range(59, -1, -1):
        y = x | 1 << i
        val = abs((a ^ y) - (b ^ y))
        if val < c and y <= r:
            c = val
            x = y
    return (c, x)


if False:
    for r in range(69):
        for a in range(69):
            for b in range(69):
                assert naive(a, b, r)[0] == smart(a, b, r)[0], (
                    a,
                    b,
                    r,
                    naive(a, b, r),
                    smart(a, b, r),
                )
else:
    for _ in range(int(input())):
        a, b, r = map(int, input().split())
        print(smart(a, b, r)[0])
