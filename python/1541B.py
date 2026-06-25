# ruff: noqa: E731, E741
from operator import itemgetter
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    sorted_enumerate = sorted(
        enumerate(map(int, input().split()), 1), key=itemgetter(1)
    )
    ans = 0
    for i, (ismall, xsmall) in enumerate(sorted_enumerate):
        if xsmall * xsmall >= n + n:
            break
        max_sum_indexes = min(ismall, n - 1) + n
        for ibig, xbig in sorted_enumerate[i + 1 :]:
            p = xsmall * xbig
            if p > max_sum_indexes:
                break
            ans += p == ismall + ibig
    print(ans)
