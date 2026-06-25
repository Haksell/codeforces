# ruff: noqa: E731, E741
for _ in range(int(input())):
    res = 0
    for y in range(10):
        for x, c in enumerate(input()):
            if c == "X":
                res += min(y + 1, 10 - y, x + 1, 10 - x)
    print(res)
