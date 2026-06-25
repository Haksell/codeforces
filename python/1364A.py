# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    if s % x != 0:
        print(n)
    else:
        lo = next((i for i in range(n) if a[i] % x != 0), None)
        if lo is None:
            print(-1)
        else:
            hi = next(i for i in reversed(range(n)) if a[i] % x != 0)
            print(max(hi, n - lo - 1))
