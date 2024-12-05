# ruff: noqa: E731, E741
from bisect import bisect_right

triangles = [
    0,
    1,
    3,
    6,
    10,
    15,
    21,
    28,
    36,
    45,
    55,
    66,
    78,
    91,
    105,
    120,
    136,
    153,
    171,
    190,
    210,
    231,
    253,
]

n, k = map(int, input().split())
t = (240 - k) / 5
res = bisect_right(triangles, t) - 1
print(min(n, res))
