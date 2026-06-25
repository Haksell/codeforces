# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, a, b, c = mir()
    r3, n = divmod(n, a + b + c)
    print(3 * r3 + (0 if n == 0 else 1 if n <= a else 2 if n <= a + b else 3))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
