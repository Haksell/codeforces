# ruff: noqa: E731, E741
for _ in range(int(input())):
    q, m = divmod(int(input()), 3)
    print(q + (m == 2), q + 1 + (m > 0), q - 1)
