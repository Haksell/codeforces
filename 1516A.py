# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n - 1):
        x = min(a[i], k)
        a[i] -= x
        a[-1] += x
        k -= x
        if k == 0:
            break
    print(*a)
