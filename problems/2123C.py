# ruff: noqa: E731, E741
from itertools import accumulate
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
    prefix_min = list(accumulate(a, min))
    suffix_max = list(accumulate(a[::-1], max))[::-1]
    print(
        "".join(
            "1" if ai == prefix_min[i] or ai == suffix_max[i] else "0"
            for i, ai in enumerate(a)
        )
    )


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
