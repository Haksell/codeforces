# ruff: noqa: E731, E741
res = [0, 2, 1, 1, 2, 2, 2]
for _ in range(int(input())):
    n = int(input())
    print(-(-n // 3) if n > 6 else res[n])
