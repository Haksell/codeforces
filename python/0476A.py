# ruff: noqa: E731, E741
n, m = map(int, input().split())
mini = (n + 1) // 2
print(next((i for i in range(mini, min(n + 1, mini + m)) if i % m == 0), -1))
