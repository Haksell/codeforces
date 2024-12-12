# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    print("YES" if n * m - 1 == k else "NO")
