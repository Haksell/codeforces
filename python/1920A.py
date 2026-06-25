# ruff: noqa: E731, E741
import math

for _ in range(int(input())):
    mini = -math.inf
    maxi = math.inf
    s = set()
    for _ in range(int(input())):
        a, x = map(int, input().split())
        match a:
            case 1:
                mini = max(mini, x)
            case 2:
                maxi = min(maxi, x)
            case 3:
                s.add(x)
    if mini > maxi:
        print(0)
    else:
        print(maxi - mini + 1 - sum(mini <= x <= maxi for x in s))
