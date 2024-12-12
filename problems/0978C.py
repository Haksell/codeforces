# ruff: noqa: E731, E741
from bisect import bisect_left
from itertools import accumulate

input()
a = list(map(int, input().split()))
acc = list(accumulate(a, initial=0))
for n in map(int, input().split()):
    room = bisect_left(acc, n)
    print(room, n - acc[room - 1])
