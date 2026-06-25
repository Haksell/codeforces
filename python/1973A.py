# ruff: noqa: E731, E741
for _ in range(int(input())):
    p1, p2, p3 = map(int, input().split())
    if (p1 ^ p2 ^ p3) & 1:
        print(-1)
    else:
        print(min(p1 + p2 + p3 >> 1, p1 + p2))
