# ruff: noqa: E731, E741
from collections import Counter

n = int(input())
s1 = Counter(map(int, input().split()))
s2 = Counter(map(int, input().split()))
s3 = Counter(map(int, input().split()))
print(list(s1 - s2).pop())
print(list(s2 - s3).pop())
