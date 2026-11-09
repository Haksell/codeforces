from bisect import bisect
from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

acc = [0] + list(accumulate(a))
for qi in q:
    print(bisect(acc, qi - 1))
