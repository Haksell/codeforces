# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    b = input().split()
    s = b[0] + "".join(y[1] if x[1] == y[0] else y for x, y in zip(b, b[1:]))
    if len(s) != n:
        s += "a"
    print(s)
