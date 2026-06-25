# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n = ir()
    if n <= 4:
        print(-1)
    else:
        res = (
            [i for i in range(2, n + 1, 2) if i != 4]
            + [4, 5]
            + [i for i in range(1, n + 1, 2) if i != 5]
        )
        print(*res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
