# ruff: noqa: E731, E741
a, b, c, d = map(int, input().split())
s = a + b + c + d
if s & 1:
    print("NO")
else:
    h = s >> 1
    print(
        "YES"
        if a == h
        or b == h
        or c == h
        or d == h
        or a + b == h
        or a + c == h
        or a + d == h
        else "NO"
    )
