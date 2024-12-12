# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    g = [input() for _ in range(4)]
    print(
        "YES"
        if any(
            (
                (g[y][x] == ".")
                + (g[y][x + 1] == ".")
                + (g[y + 1][x] == ".")
                + (g[y + 1][x + 1] == ".")
            )
            != 2
            for y in range(3)
            for x in range(3)
        )
        else "NO"
    )


if __name__ == "__main__":
    main()
