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
    n, v = mir()
    a1, a2 = [], []
    i1, i2 = [], []
    for i in range(n):
        t, p = mir()
        if t == 1:
            a1.append(p)
            i1.append(i)
        else:
            a2.append(p)
            i2.append(i)
    acc1 = list(accumulate(sorted(a1, reverse=True), initial=0))
    acc2 = list(accumulate(sorted(a2, reverse=True), initial=0))
    best = (0, 0, 0)
    for n2 in range(min(v // 2, len(a2)) + 1):
        n1 = min(v - 2 * n2, len(a1))
        best = max(best, (acc1[n1] + acc2[n2], n1, n2))
    ans, n1, n2 = best
    print(ans)
    ii1 = sorted(range(len(a1)), key=a1.__getitem__)[len(a1) - n1 :]
    ii2 = sorted(range(len(a2)), key=a2.__getitem__)[len(a2) - n2 :]
    print(*[i1[i] + 1 for i in ii1], *[i2[i] + 1 for i in ii2])


if __name__ == "__main__":
    main()
