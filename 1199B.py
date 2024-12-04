# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    h, l = mir()
    x = (l**2 - (h**2)) / (2 * h)
    print(x)


if __name__ == "__main__":
    main()
