# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n, g):
    if g[0][0] == "." or g[0][-1] == "." or g[-1][0] == "." or g[-1][-1] == ".":
        return False
    for y in range(1, n - 1):
        for x in range(1, n - 1):
            if (
                g[y][x] == "."
                and g[y - 1][x] == "."
                and g[y + 1][x] == "."
                and g[y][x - 1] == "."
                and g[y][x + 1] == "."
            ):
                g[y][x] = g[y - 1][x] = g[y + 1][x] = g[y][x - 1] = g[y][x + 1] = "#"
    return all(c == "#" for r in g for c in r)


def main():
    n = ir()
    g = [list(input()) for _ in range(n)]
    print("YES" if solve(n, g) else "NO")


if __name__ == "__main__":
    main()
