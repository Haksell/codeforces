# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    cnt = a.count(m)
    if cnt == n:
        print(-1)
    else:
        print(n - cnt, cnt)
        print(*[ai for ai in a if ai != m])
        print(*([m] * cnt))
