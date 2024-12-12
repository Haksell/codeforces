# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    q, r = divmod(n, 2050)
    print(-1 if r else sum(map(int, str(q))))
