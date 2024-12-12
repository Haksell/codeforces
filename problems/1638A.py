# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    i = next((i for i, pi in enumerate(p) if i + 1 != pi), None)
    if i is not None:
        x = p.index(i + 1)
        p[i : x + 1] = p[i : x + 1][::-1]
    print(*p)
