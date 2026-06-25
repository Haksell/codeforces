# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    o = c = 0
    for x in input():
        if x == "(":
            o += 1
        elif c < o:
            c += 1
    print(2 * c)


if __name__ == "__main__":
    main()
