# ruff: noqa: E731, E741
from bisect import bisect_right
from itertools import accumulate
from operator import itemgetter
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

INF = 1 << 50


def f(hw_pref, ep_pref, max_start, deadlines, t):
    forced = bisect_right(max_start, t)
    if deadlines[forced - 1] > t:
        new_t = min(t, max_start[forced - 1])
    else:
        new_t = t
    before = bisect_right(deadlines, new_t)
    start_problems_time = hw_pref[before]
    series_time = new_t - start_problems_time
    return bisect_right(ep_pref, series_time) - 1


def solve():
    read()
    a = lmir()
    d = lmir()
    episodes = lmir()
    homework = sorted(zip(a, d), key=itemgetter(1))
    hw_pref = list(accumulate((ai for ai, _ in homework), initial=0))
    ep_pref = list(accumulate(episodes, initial=0))
    deadlines = []
    max_start = []
    d = INF
    max_start.append(d)
    deadlines.append(d)
    for duration, deadline in reversed(homework):
        d = min(deadline, d) - duration
        max_start.append(d)
        deadlines.append(d + duration)
    max_start.reverse()
    deadlines.reverse()
    print(*[f(hw_pref, ep_pref, max_start, deadlines, t) for t in mir()])


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
