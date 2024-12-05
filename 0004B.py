# ruff: noqa: E731, E741
from operator import itemgetter

d, st = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(d)]
mini = sum(map(itemgetter(0), lst))
maxi = sum(map(itemgetter(1), lst))
if mini <= st <= maxi:
    print("YES")
    ans = []
    diff = st - mini
    for a, b in lst:
        nxt = min(a + diff, b)
        ans.append(nxt)
        diff -= nxt - a
    print(*ans)
else:
    print("NO")
