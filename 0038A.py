# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    read()
    d = lmir()
    a, b = mir()
    print(sum(d[a - 1 : b - 1]))


if __name__ == "__main__":
    main()
