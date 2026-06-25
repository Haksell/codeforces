# ruff: noqa: E731, E741
IMPOSSIBLE = (1, 2, 4)
for _ in range(int(input())):
    n = int(input())
    q, r = divmod(n, 3)
    if n in IMPOSSIBLE:
        print(-1)
    elif r == 0:
        print(q, 0, 0)
    elif r == 1:
        print(q - 2, 0, 1)
    else:
        print(q - 1, 1, 0)
