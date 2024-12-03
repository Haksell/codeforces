# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n = ir()
    a = lmir()
    b = lmir()
    i = max(range(n), key=lambda i: min(a[i], b[i]))
    print(sum(map(max, a, b)) + min(a[i], b[i]))


def test():
    pass


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        for _ in rir():
            solve()
