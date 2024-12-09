# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = []
    last = None
    for b in map(int, input()):
        x = 0 if last == b + 1 else 1
        a.append(x)
        last = b + x
    print("".join(map(str, a)))
