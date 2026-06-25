# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def direc(x0, y0, x1, y1):
    if x0 == x1:
        return "NORTH" if y1 > y0 else "SOUTH"
    else:
        return "EAST" if x1 > x0 else "WEST"


def main():
    n = ir()
    xy = [lmir() for _ in range(n + 1)]
    r = 0
    for i in range(n - 1):
        x0, y0 = xy[i]
        x1, y1 = xy[i + 1]
        x2, y2 = xy[i + 2]
        d01 = direc(x0, y0, x1, y1)
        d12 = direc(x1, y1, x2, y2)
        r += d01 == "NORTH" and d12 == "WEST"
        r += d01 == "EAST" and d12 == "NORTH"
        r += d01 == "SOUTH" and d12 == "EAST"
        r += d01 == "WEST" and d12 == "SOUTH"
    print(r)


if __name__ == "__main__":
    main()
