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
        l, r = mir()
        x = 0
        while r:
            x += r - l
            l //= 10
            r //= 10
        print(x)


if __name__ == "__main__":
    main()
