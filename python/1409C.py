# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    d = y - x
    k = next(i for i in range(1, d + 1) if d % i == 0 and i * (n - 1) >= d)
    m = y - k * (n - 1)
    if m <= 0:
        m = m % k or k
    print(*range(m, m + k * n, k))
