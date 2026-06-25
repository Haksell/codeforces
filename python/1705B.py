# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a[:-1])
    i = next((i for i in range(n) if a[i] != 0), n)
    print(s + a[i:-1].count(0))
