# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    n = ir()
    if n % 3 != 2:
        print(1, 1, n - 2)
    else:
        print(1, 2, n - 3)


if __name__ == "__main__":
    main()
