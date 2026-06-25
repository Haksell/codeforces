# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n = ir()
    max_height = max_width = 0
    for _ in range(n):
        w, h = mir()
        max_height = max(max_height, h)
        max_width = max(max_width, w)
    print((max_width + max_height) * 2)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
