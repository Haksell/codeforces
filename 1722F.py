# ruff: noqa: E731, E741
def f(y, x):
    return 0 <= y < h and 0 <= x < w and g[y][x]


def check(y, x, shape, nocheck):
    if any(not f(yi, xi) for yi, xi in shape):
        return False
    for yi in range(y - 1, y + 3):
        for xi in range(x - 1, x + 3):
            pair = (yi, xi)
            if pair in shape or pair == nocheck:
                continue
            if f(yi, xi):
                return False
    return True


for _ in range(int(input())):
    h, w = map(int, input().split())
    g = [[c == "*" for c in input()] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            for shape, nocheck in [
                ([(y, x), (y + 1, x), (y + 1, x + 1)], (y - 1, x + 2)),
                ([(y, x + 1), (y + 1, x), (y + 1, x + 1)], (y - 1, x - 1)),
                ([(y, x), (y, x + 1), (y + 1, x + 1)], (y + 2, x - 1)),
                ([(y, x), (y, x + 1), (y + 1, x)], (y + 2, x + 2)),
            ]:
                if check(y, x, shape, nocheck):
                    for yi, xi in shape:
                        g[yi][xi] = False
    print("NO" if any(map(any, g)) else "YES")
