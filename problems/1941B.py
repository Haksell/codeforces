# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n - 1):
        if a[i - 1] > 0:
            a[i] -= 2 * a[i - 1]
            a[i + 1] -= a[i - 1]
            a[i - 1] = 0
    print("NO" if any(a) else "YES")
