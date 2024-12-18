# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        m, a, b, c = mir()
        x = max(0, m - a) + max(0, m - b)
        x = max(0, x - c)
        print(2 * m - x)


if __name__ == "__main__":
    main()
