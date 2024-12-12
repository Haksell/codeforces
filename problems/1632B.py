# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    cost = 1 << ((n - 1).bit_length() - 1)
    print(*range(1, cost), 0, *range(cost, n))
