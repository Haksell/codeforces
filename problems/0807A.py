# ruff: noqa: E731, E741
import math
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    res = "maybe"
    prev = math.inf
    for _ in rir():
        a, b = mir()
        if a != b:
            res = "rated"
            break
        if a > prev:
            res = "unrated"
        prev = a
    print(res)


if __name__ == "__main__":
    main()
