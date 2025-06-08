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
    if n & 1:
        res = [n // 2 + i // 2 + 2 if i & 1 else i // 2 + 1 for i in range(n)]
        print(*res)
    else:
        print(-1)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
