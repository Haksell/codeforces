# ruff: noqa: E731, E741
n, m = map(int, input().split())
q, r = divmod(m, n)
if r != 0:
    print(-1)
else:
    res = 0
    while q & 1 == 0:
        q >>= 1
        res += 1
    while q % 3 == 0:
        q //= 3
        res += 1
    print(res if q == 1 else -1)
