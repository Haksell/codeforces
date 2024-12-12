# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in reversed(range(n)):
        if i + a[i] < n:
            a[i] += a[i + a[i]]
    print(max(a))
