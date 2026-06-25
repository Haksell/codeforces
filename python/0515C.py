# ruff: noqa: E731, E741
from math import prod

FACTORIALS = [1]
for i in range(1, 10):
    FACTORIALS.append(FACTORIALS[-1] * i)
input()
p = prod(FACTORIALS[ord(x) - 48] for x in input())
ans = []
for i in [7, 5, 3, 2]:
    while p % FACTORIALS[i] == 0:
        p //= FACTORIALS[i]
        ans.append(i)
print("".join(map(str, ans)))
