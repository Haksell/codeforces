# ruff: noqa: E731, E741
from itertools import accumulate
from operator import add
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


"""
1 2 3



"""


def main():
    n, m, k = mir()
    a = lmir()
    lrd = [tuple(mir()) for _ in range(m)]

    ops = [0] * (m + 1)
    for _ in range(k):
        x, y = mir()
        ops[x - 1] += 1
        ops[y] -= 1
    acc_ops = list(accumulate(ops))

    changes = [0] * (n + 1)
    for i, (l, r, d) in enumerate(lrd):
        changes[l - 1] += d * acc_ops[i]
        changes[r] -= d * acc_ops[i]
    acc_changes = list(accumulate(changes))

    print(*map(add, a, acc_changes))


if __name__ == "__main__":
    main()
