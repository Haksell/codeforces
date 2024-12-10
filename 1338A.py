# ruff: noqa: E731, E741
from math import inf

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    maxi = -inf
    ans = 0
    for ai in a:
        ans = max(ans, maxi - ai)
        maxi = max(maxi, ai)
    print(ans.bit_length())
