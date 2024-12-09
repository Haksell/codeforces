# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = sorted(a)
    print(
        max(
            d[0] * d[1] * d[2] * d[3] * d[4],
            d[0] * d[1] * d[2] * d[3] * d[-1],
            d[0] * d[1] * d[2] * d[-2] * d[-1],
            d[0] * d[1] * d[-3] * d[-2] * d[-1],
            d[0] * d[-4] * d[-3] * d[-2] * d[-1],
            d[-5] * d[-4] * d[-3] * d[-2] * d[-1],
        )
    )
