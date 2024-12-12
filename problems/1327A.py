# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    print("YES" if n & 1 == k & 1 and n >= k * k else "NO")
