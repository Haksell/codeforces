# ruff: noqa: E731, E741
from bisect import bisect
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n, _, _ = mir()
        b = sorted(mir())
        for d in mir():
            if d < b[0]:
                print(b[0] - 1)
            elif d > b[-1]:
                print(n - b[-1])
            else:
                i = bisect(b, d)
                w = b[i] - b[i - 1]
                print(w >> 1)


if __name__ == "__main__":
    main()
