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
        acc = list(accumulate(a, initial=0))
        res = 0
        for k in range(1, n // 2 + 1):
            if n % k != 0:
                continue
            trucks = [acc[i] - acc[i - k] for i in range(k, len(acc), k)]
            res = max(res, max(trucks) - min(trucks))
        print(res)


if __name__ == "__main__":
    main()
