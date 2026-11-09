import math

for _ in range(int(input())):
    min10 = min01 = min11 = math.inf
    for _ in range(int(input())):
        t, s = map(int, input().split())
        if s == 10:
            min10 = min(t, min10)
        if s == 1:
            min01 = min(t, min01)
        if s == 11:
            min11 = min(t, min11)
    res = min(min11, min10 + min01)
    print(-1 if res is math.inf else res)
