# ruff: noqa: E731, E741
from bisect import bisect
from itertools import accumulate
from operator import itemgetter

n, d = map(int, input().split())
friends = sorted(
    [tuple(map(int, input().split())) for _ in range(n)], key=itemgetter(0)
)
aff = list(accumulate([s for _, s in friends], initial=0))
ans = 0
for i, (m, s) in enumerate(friends):
    j = bisect(friends, (m + d - 0.5, None))
    x = aff[j] - aff[i]
    ans = max(ans, x)
print(ans)
