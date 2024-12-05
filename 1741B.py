# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(2, 1)
    elif n == 3:
        print(-1)
    else:
        print(*range(3, n + 1), 1, 2)
