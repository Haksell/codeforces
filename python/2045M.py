# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def main():
    h, w = mir()
    g = [input() for _ in range(h)]
    m = sum(c != "." for r in g for c in r)
    results = [[[-1] * 4 for _ in range(w)] for _ in range(h)]
    path = set()
    for y in range(h):
        for x in range(w):
            for d in range(4):
                if results[y][x][d] != -1:
                    continue
                if not (
                    (x == 0 and d == EAST)
                    or (x == w - 1 and d == WEST)
                    or (y == 0 and d == SOUTH)
                    or (y == h - 1 and d == NORTH)
                ):
                    continue
                xx, yy, dd = x, y, d
                ooga = -1
                while (x, y, d) not in path and 0 <= x < w and 0 <= y < h:
                    # if results[y][x][d] != -1:
                    #     print(x, y, d, results[y][x][d])
                    #     ooga = results[y][x][d]
                    #     break
                    path.add((x, y, d))
                    if g[y][x] == "/":
                        if d == NORTH:
                            d = EAST
                        elif d == EAST:
                            d = NORTH
                        elif d == SOUTH:
                            d = WEST
                        elif d == WEST:
                            d = SOUTH
                    if g[y][x] == "\\":
                        if d == NORTH:
                            d = WEST
                        elif d == WEST:
                            d = NORTH
                        elif d == SOUTH:
                            d = EAST
                        elif d == EAST:
                            d = SOUTH
                    dx, dy = DIRS[d]
                    x += dx
                    y += dy
                x, y, d = xx, yy, dd
                xy = {(xx, yy) for (xx, yy, _) in path}
                t = sum(g[yy][xx] != "." for xx, yy in xy)
                # print(path, t)
                ok = ooga if ooga != -1 else int(t == m)
                for xx, yy, dd in path:
                    # print(x, y, d, ok)
                    results[yy][xx][dd] = ok
                path.clear()
    # print(*results, sep="\n")
    out = []
    for x in range(w):
        if results[0][x][SOUTH]:
            out.append(f"N{x+1}")
        if results[-1][x][NORTH]:
            out.append(f"S{x+1}")
    for y in range(h):
        if results[y][0][EAST]:
            out.append(f"W{y+1}")
        if results[y][-1][WEST]:
            out.append(f"E{y+1}")
    print(len(out))
    if out:
        print(*out)


if __name__ == "__main__":
    main()
