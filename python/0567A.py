# ruff: noqa: E731, E741
n = int(input())
xs = list(map(int, input().split()))
for i, x in enumerate(xs):
    print(
        xs[1] - x
        if i == 0
        else x - xs[-2]
        if i == n - 1
        else min(x - xs[i - 1], xs[i + 1] - x),
        max(x - xs[0], xs[-1] - x),
    )
