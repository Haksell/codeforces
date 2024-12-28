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
    n = ir()
    once = [False] * (2 * n + 1)
    twice = [False] * (2 * n + 1)
    q = []
    for _ in range(n):
        l, r = mir()
        if l == r:
            if once[l]:
                twice[l] = True
            else:
                once[l] = True
        q.append((l, r))
    acc = list(accumulate(once))
    res = []
    for l, r in q:
        if l == r:
            res.append(not twice[l])
        else:
            res.append(acc[r] - acc[l - 1] != r - l + 1)
    print("".join("1" if x else "0" for x in res))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
