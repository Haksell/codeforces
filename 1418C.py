# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n, a):
    r = i = 0
    while i < n:
        r += a[i]
        i += 1
        if i >= n - 2:
            break
        if a[i] == 0 and a[i + 1] == 1:
            i += 1
        if i >= n - 2:
            break
        i += 1
        if a[i] == 1:
            i += 1
    return r


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        print(solve(n, a))


if __name__ == "__main__":
    main()

"""

5
0 0 0 0 0
"""
