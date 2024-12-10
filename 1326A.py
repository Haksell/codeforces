# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    print(-1 if n == 1 else "5" * (n - 1) + "4")
