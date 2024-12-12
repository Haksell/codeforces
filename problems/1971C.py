# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c, d = (int(x) - 1 for x in input().split())
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    c_between = a < c < b
    d_between = a < d < b
    print("YES" if c_between ^ d_between else "NO")
