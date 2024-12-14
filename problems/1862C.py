# ruff: noqa: E731, E741
from itertools import accumulate
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        if a[0] != n:
            print("NO")
            continue
        b = [0] * n
        b[0] = n
        for ai in a:
            if ai < n:
                b[ai] -= 1
        c = list(accumulate(b))
        print("YES" if a == c else "NO")


if __name__ == "__main__":
    main()

"""
...
...
.....
.....
.....
"""
