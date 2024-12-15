# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def ceil_div(num, den):
    return -(-num // den)


def main():
    n, m, a = mir()
    print(ceil_div(n, a) * ceil_div(m, a))


if __name__ == "__main__":
    main()
