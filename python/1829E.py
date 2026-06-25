# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def depth(g, h, w, x, y):
    s = [(x, y)]
    v = g[y][x]
    g[y][x] = 0
    while s:
        x, y = s.pop()
        for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= x < w and 0 <= y < h and g[y][x]:
                v += g[y][x]
                g[y][x] = 0
                s.append((x, y))
    return v


def main():
    for _ in rir():
        h, w = mir()
        g = [lmir() for _ in range(h)]
        r = 0
        for y in range(h):
            for x in range(w):
                if not g[y][x]:
                    continue
                r = max(r, depth(g, h, w, x, y))
        print(r)


if __name__ == "__main__":
    main()
