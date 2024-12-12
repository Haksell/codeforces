# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, a, b, c, d = map(int, input().split())
    min1 = (a - b) * n
    max1 = (a + b) * n
    min2 = c - d
    max2 = c + d
    print("No" if max2 < min1 or min2 > max1 else "Yes")
