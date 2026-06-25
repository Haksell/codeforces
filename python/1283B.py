# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    q, r = divmod(n, k)
    print(q * k + min(r, k >> 1))
