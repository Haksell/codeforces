# ruff: noqa: E731, E741
from itertools import repeat

for _ in range(int(input())):
    n, k = map(int, input().split())
    if n & 1 == k & 1 and n >= k:
        print("YES")
        print(*repeat(1, k - 1), n + 1 - k)
    elif n & 1 == 0 and k & 1 == 1 and n >= 2 * k:
        print("YES")
        print(*repeat(2, k - 1), n + 2 - 2 * k)
    else:
        print("NO")
