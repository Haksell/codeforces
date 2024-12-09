# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    ops = []
    a = list(range(1, n + 1))
    for _ in range(n - 1):
        x1 = a.pop()
        x2 = a.pop()
        ops.append((x1, x2))
        a.append(-~(x1 + x2) >> 1)
    print(a.pop())
    for x1, x2 in ops:
        print(x1, x2)
