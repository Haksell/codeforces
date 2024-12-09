# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, c0, c1, h = map(int, input().split())
    s = input()
    n0 = s.count("0")
    n1 = n - n0
    print(
        h * n1 + n * c0
        if c0 + h < c1
        else h * n0 + n * c1
        if c1 + h < c0
        else n0 * c0 + n1 * c1
    )
