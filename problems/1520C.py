# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        l = list(range(1, n * n + 1, 2)) + list(range(2, n * n + 1, 2))
        for y in range(n):
            print(*l[y * n : (y + 1) * n])
