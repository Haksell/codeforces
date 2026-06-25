# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    r = []
    s = set()
    for ai in a:
        if ai not in s:
            s.add(ai)
            r.append(ai)
    print(*r)
