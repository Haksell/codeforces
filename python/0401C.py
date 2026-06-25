# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    z, o = mir()
    if z > o + 1 or o > 2 * z + 2:
        print(-1)
    elif z == o + 1:
        print("01" * o + "0")
    elif o >= 2 * z:
        print("110" * z + "1" * (o - 2 * z))
    else:
        pairs = o - z
        singles = z - pairs
        print("110" * pairs + "10" * singles)


if __name__ == "__main__":
    main()
