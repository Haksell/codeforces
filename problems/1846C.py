# ruff: noqa: E731, E741
from itertools import accumulate, takewhile
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n, _, h = mir()
        scores = []
        for i in range(n):
            t = lmir()
            acc = list(takewhile(lambda t: t <= h, accumulate(sorted(t))))
            scores.append((-len(acc), sum(acc), i))
        scores.sort()
        print(next(rank for rank, (_, _, i) in enumerate(scores, 1) if i == 0))


if __name__ == "__main__":
    main()
