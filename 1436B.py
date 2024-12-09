# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        ans[i][i] = 1
        ans[i][(i + 1) % n] = 1
    for row in ans:
        print(*row)
