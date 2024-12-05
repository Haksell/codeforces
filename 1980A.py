# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    _, m = map(int, input().split())
    cnt = Counter(input())
    print(sum(max(0, m - cnt[x]) for x in "ABCDEFG"))
