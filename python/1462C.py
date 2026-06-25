# ruff: noqa: E731, E741
for _ in range(int(input())):
    x = int(input())
    if x > 45:
        print(-1)
        continue
    l = []
    for i in range(9, 0, -1):
        l.append(min(i, x))
        x -= i
        if x <= 0:
            break
    print(*reversed(l), sep="")
