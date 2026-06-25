# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, x = mir()
    a = lmir()
    if 1 not in a:
        return True
    i = a.index(1)
    j = next(n - j - 1 for j, b in enumerate(reversed(a)) if b)
    return j - i < x


def main():
    for _ in rir():
        print("YES" if solve() else "NO")


if __name__ == "__main__":
    main()
