# ruff: noqa: E731, E741
from collections import defaultdict
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        _, x, y = mir()
        m = defaultdict(int)
        r = 0
        a = lmir()
        for ai in a:
            r += m[-ai % x, ai % y]
            m[ai % x, ai % y] += 1
        print(r)


if __name__ == "__main__":
    main()
