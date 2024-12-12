# ruff: noqa: E731, E741
n, k = map(int, input().split())
a = list(map(int, input().split()))
i = next((i for i in range(n) if a[i] > k), -1)
if i == -1:
    print(n)
else:
    j = next(j for j in reversed(range(n)) if a[j] > k)
    print(n - j + i - 1)
