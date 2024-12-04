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
    n = ir()
    a = lmir()
    acc = list(accumulate(max(ai, 0) for ai in a))
    negative_idx = sorted(
        [i for i, ai in enumerate(a) if ai < 0], key=a.__getitem__, reverse=True
    )
    res = sum(ai >= 0 for ai in a)

    for i in negative_idx:
        if all(acc[j] + a[i] >= 0 for j in range(i, n)):
            res += 1
            for j in range(i, n):
                acc[j] += a[i]
    print(res)


if __name__ == "__main__":
    main()
