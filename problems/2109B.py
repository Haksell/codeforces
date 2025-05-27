# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def f(n):
    return (n - 1).bit_length()


def solve():
    h, w, y, x = mir()
    if h == w == 1:
        return 0
    y -= 1
    x -= 1
    res = 0
    while h > 1 or w > 1:
        ww = min(x + 1, w - x)
        hh = min(y + 1, h - y)
        dw = f(w) - f(ww)
        dh = f(h) - f(hh)
        if dw > dh:
            w = ww
        else:
            h = hh
        x = w >> 1
        y = h >> 1
        res += 1
    return res


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
