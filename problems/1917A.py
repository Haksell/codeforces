# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    neg = sum(ai < 0 for ai in a)
    if neg & 1 or 0 in a:
        print(0)
    else:
        print(1)
        print(1, 0)
