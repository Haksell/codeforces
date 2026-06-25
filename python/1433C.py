# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    print(
        next(
            (
                i + 1
                for i, ai in enumerate(a)
                if ai == m and (i > 0 and ai > a[i - 1] or i < n - 1 and ai > a[i + 1])
            ),
            -1,
        )
    )
