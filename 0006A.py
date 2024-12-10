# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    a, b, c, d = sorted(mir())
    print(
        "TRIANGLE"
        if a + b > c or b + c > d
        else "SEGMENT"
        if a + b == c or b + c == d
        else "IMPOSSIBLE"
    )


if __name__ == "__main__":
    main()
