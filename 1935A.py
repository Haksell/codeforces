# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = input()
    r = s[::-1]
    if s <= r:
        print(s)
    else:
        print(r + s)
