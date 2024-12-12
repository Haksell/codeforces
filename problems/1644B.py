# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    for i in range(1, n + 1):
        print(i, *[j for j in range(n, 0, -1) if i != j])
