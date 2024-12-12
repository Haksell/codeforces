# ruff: noqa: E731, E741
for _ in range(int(input())):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())
    d = p1 - p2
    if d > 6:
        print(">")
    elif d < -6:
        print("<")
    else:
        if d >= 0:
            x1 *= 10**d
        else:
            x2 *= 10**-d
        print(">" if x1 > x2 else "<" if x1 < x2 else "=")
