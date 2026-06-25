# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    z, o, k = mir()
    if abs(z - o) > k or k > max(z, o):
        return "-1"
    elif z >= o:
        return "0" * k + "10" * (z - k) + "1" * (o - (z - k))
    else:
        return "1" * k + "01" * (o - k) + "0" * (z - (o - k))


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
