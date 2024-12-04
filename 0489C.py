def get_min(m, s):
    lmin = [0] * m
    lmin[0] = 1
    s -= 1
    i = m - 1
    while s > 0:
        d = min(9, s)
        lmin[i] += d
        s -= d
        i -= 1
    return int("".join(map(str, lmin)))


def get_max(m, s):
    lmax = []
    for i in range(m):
        d = min(9, s)
        lmax.append(d)
        s -= d
    return int("".join(map(str, lmax)))


m, s = map(int, input().split())
if s == 0:
    if m == 1:
        print(0, 0)
    else:
        print(-1, -1)
else:
    if s > 9 * m:
        print(-1, -1)
    else:
        print(get_min(m, s), get_max(m, s))
