# ruff: noqa: E731, E741
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        b = lmir()
        x = randint(1, 1 << 30)
        print("YES" if len({bi + x for bi in b}) != n else "NO")


if __name__ == "__main__":
    main()
