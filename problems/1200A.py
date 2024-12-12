# ruff: noqa: E731, E741
a = [0] * 10
input()
for c in input():
    if c == "L":
        a[next(i for i, ai in enumerate(a) if ai == 0)] = 1
    elif c == "R":
        a[next(i for i, ai in reversed(list(enumerate(a))) if ai == 0)] = 1
    else:
        a[int(c)] = 0
print(*a, sep="")
