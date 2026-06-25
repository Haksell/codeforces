# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    np = [ai for ai in a if ai <= 0]
    if len(np) == n:
        print(n)
    else:
        nxt = a[len(np)]
        print(len(np) + all(y - x >= nxt for x, y in zip(np, np[1:])))
