# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b = map(int, input().split())
    if b == 1:
        print("NO")
    else:
        print("YES")
        m = a * b * 2
        print(a, m - a, m)
