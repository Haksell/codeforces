# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    read()
    a = lmir()
    print("YES" if any(2 * min(x, y) > max(x, y) for x, y in zip(a, a[1:])) else "NO")


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
