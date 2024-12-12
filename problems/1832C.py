# ruff: noqa: E731, E741
from itertools import groupby
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        read()
        a = [k for k, _ in groupby(mir())]
        if len(a) == 1:
            print(1)
            continue
        print(
            2
            + sum(
                a[i - 1] > a[i] < a[i + 1] or a[i - 1] < a[i] > a[i + 1]
                for i in range(1, len(a) - 1)
            )
        )


if __name__ == "__main__":
    main()
