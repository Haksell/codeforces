# ruff: noqa: E731, E741
from itertools import islice


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mini = maxi = a[0]
    for ai in islice(a, 1, None):
        if ai == mini - 1:
            mini = ai
        elif ai == maxi + 1:
            maxi = ai
        else:
            print("NO")
            break
    else:
        print("YES")
