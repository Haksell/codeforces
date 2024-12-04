# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    p, m, c, k, r, v = map(int, sys.stdin.read().split())
    print(min(p // k, m // r, c // v))


if __name__ == "__main__":
    main()