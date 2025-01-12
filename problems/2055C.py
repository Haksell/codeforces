# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    h, _ = mir()
    path = input()
    grid = [lmir() for _ in range(h)]
    row_sums = list(map(sum, grid))
    col_sums = list(map(sum, zip(*grid)))
    x = y = 0
    for d in path:
        if d == "R":
            grid[y][x] = -col_sums[x]
            row_sums[y] -= col_sums[x]
            x += 1
        else:
            grid[y][x] = -row_sums[y]
            col_sums[x] -= row_sums[y]
            y += 1
    grid[-1][-1] = -row_sums[-1]
    for row in grid:
        print(*row)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
