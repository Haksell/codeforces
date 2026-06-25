# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("NO" if all(y >= x for x, y in zip(a, a[1:])) else "YES")
