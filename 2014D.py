# ruff: noqa: E731, E741
from itertools import accumulate
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


# def main():
#     for _ in rir():
#         n, d, k = mir()
#         a = [0] * (n + 1)
#         for _ in range(k):
#             l, r = mir()
#             a[l - 1] += 1
#             a[r] -= 1
#         a.pop()
#         jobs = list(accumulate(a))
#         print(jobs)
#         ranges = [sum(jobs[:d])]
#         for i in range(d, n):
#             ranges.append(ranges[-1] + jobs[i] - jobs[i - d])
#         print(ranges)
#         print(
#             max(range(len(ranges)), key=ranges.__getitem__) + 1,
#             min(range(len(ranges)), key=ranges.__getitem__) + 1,
#         )
#         print()


def main():
    for _ in rir():
        n, d, k = mir()
        a = [0] * (n + 1)
        start = [0] * n
        for _ in range(k):
            l, r = mir()
            start[l - 1] += 1
            a[l - 1] += 1
            a[r] -= 1
        a.pop()
        start = list(accumulate(start))
        current = list(accumulate(a))
        # print(current)
        # print(start)
        ranges = [current[i] + start[i + d - 1] - start[i] for i in range(n - d + 1)]
        # print(ranges)
        print(
            max(range(len(ranges)), key=ranges.__getitem__) + 1,
            min(range(len(ranges)), key=ranges.__getitem__) + 1,
        )
        # print()


if __name__ == "__main__":
    main()

"""
122111221
"""
