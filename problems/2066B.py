# ruff: noqa: E731, E741
from collections import Counter
from heapq import heapify, heappop
from itertools import combinations, count
from random import choices, randint, seed
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def mex(a):
    s = set(a)
    return next(i for i in count() if i not in s)


def naive_is_magical(a):
    for i in range(1, len(a)):
        left = a[:i]
        right = a[i:]
        if min(left) < mex(right):
            return False
    return True


def naive(n, a):
    res = 0
    for r in range(1, n + 1):
        for comb in combinations(range(n), r=r):
            ss = [a[i] for i in comb]
            if naive_is_magical(ss):
                res = r
                break
    return res


def smart_is_magical(a):
    left_rm = Counter()
    left = a.copy()
    heapify(left)

    seen_right = [False] * len(a)
    mex_right = 0

    for ai in a[:0:-1]:
        left_rm[ai] += 1
        while left_rm[left[0]]:
            left_rm[heappop(left)] -= 1

        if ai < len(a):
            seen_right[ai] = True
        while mex_right < len(a) and seen_right[mex_right]:
            mex_right += 1

        if left[0] < mex_right:
            return False
    return True


def smart(n, a):
    if 0 not in a:
        return n
    i = a.index(0)
    b = a[: i + 1] + [ai for ai in a[i + 1 :] if ai != 0]
    return len(b) if smart_is_magical(b) else len(b) - 1


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        print(smart(n, a))


def test():
    seed(0)
    for test_case in range(1000):
        n = randint(1, 20)
        a = choices(range(n + 2), k=n)
        rn = naive(n, a)
        rs = smart(n, a)
        if rn != rs:
            print(test_case, n, a, rn, rs)
            return


if __name__ == "__main__":
    if sys.stdin.isatty():
        test()
    else:
        main()
