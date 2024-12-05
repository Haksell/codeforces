# ruff: noqa: E731, E741
from collections import Counter

_, k = map(int, input().split())
cnt = Counter(input())
print(k * min(cnt[chr(i + 65)] for i in range(k)))
