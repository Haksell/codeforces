# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    res = n = 0
    for c in input():
        if c == "(":
            n += 1
        else:
            n -= 1
            res = max(res, -n)
    print(res)
