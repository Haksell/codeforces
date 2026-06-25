# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input()))
    a = []
    b = []
    for i, d in enumerate(l):
        if d == 0:
            a.append(0)
            b.append(0)
        elif d == 2:
            a.append(1)
            b.append(1)
        else:
            a.append(1)
            b.append(0)
            a.extend([0] * (n - i - 1))
            b.extend(l[i + 1 :])
            break
    print(*a, sep="")
    print(*b, sep="")
