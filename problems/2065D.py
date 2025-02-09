# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, m = mir()
    a = sorted([lmir() for _ in range(n)], key=sum, reverse=True)
    a = [x for row in a for x in row]
    print(sum((n * m - i) * ai for i, ai in enumerate(a)))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
