# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = sum(a) // n
    margin = 0
    for ai in a:
        margin += ai - m
        if margin < 0:
            print("NO")
            break
    else:
        print("YES")
