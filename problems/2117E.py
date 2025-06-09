# ruff: noqa: E731, E741
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n, a, b):
    f = randint(1, 1 << 30)
    a = [ai + f for ai in a]
    b = [bi + f for bi in b]

    prev_a = prev_b = None
    seen_a = set()
    seen_b = set()

    for i in reversed(range(n)):
        if (
            a[i] == b[i]
            or a[i] in seen_a
            or b[i] in seen_b
            or a[i] in seen_b
            or b[i] in seen_a
            or a[i] == prev_a
            or b[i] == prev_b
        ):
            return i + 1

        if i != n - 1:
            seen_a.add(prev_a)
            seen_b.add(prev_b)
        prev_a = a[i]
        prev_b = b[i]

    return 0


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        b = lmir()
        print(solve(n, a, b))


if __name__ == "__main__":
    main()
