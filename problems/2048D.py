# ruff: noqa: E731, E741
from bisect import bisect_left
from itertools import accumulate
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def get_rank(smarter, easiest):
    i_beat = bisect_left(smarter, easiest)
    return len(smarter) - i_beat


def solve_one(acc_beats, k, m):
    res = contests = m // k
    for i in range(k, k * contests + 1, k):
        res += bisect_left(acc_beats, i)
    return res


def solve():
    n, m = mir()
    kev, *others = mir()
    smarter = sorted(ri for ri in others if ri > kev)
    p = lmir()
    beats = [0] * (n + 1)
    for pi in p:
        rank = (
            0 if pi <= kev or not smarter or pi > smarter[-1] else get_rank(smarter, pi)
        )
        beats[rank] += 1
    acc_beats = list(accumulate(beats))
    print(*[solve_one(acc_beats, k, m) for k in range(1, m + 1)])


def main():
    for _ in rir():
        solve()


def test():
    pass


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
