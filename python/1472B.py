# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    o = a.count(1)
    t = a.count(2)
    print("NO" if s & 1 or (o == 0 and t & 1) else "YES")
