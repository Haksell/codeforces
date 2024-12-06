# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    if n & 1 == 0:
        print(0, 0, n >> 1)
    else:
        print(-1)
