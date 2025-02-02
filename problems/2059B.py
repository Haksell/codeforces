# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, k = mir()
    a = lmir()
    if any(ai != 1 for ai in a[1 : len(a) - k + 2]):
        return 1
    if n == k and all(i == ai for i, ai in enumerate(a[1::2], 1)):
        return k // 2 + 1
    return 2


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
