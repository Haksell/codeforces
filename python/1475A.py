# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    print("YES" if n & (n - 1) else "NO")
