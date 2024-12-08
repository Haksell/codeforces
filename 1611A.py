# ruff: noqa: E731, E741
for _ in range(int(input())):
    l = list(map(int, input()))
    print(
        0
        if l[-1] & 1 == 0
        else 1
        if l[0] & 1 == 0
        else 2
        if any(n & 1 == 0 for n in l)
        else -1
    )
