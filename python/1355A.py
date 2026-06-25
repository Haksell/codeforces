# ruff: noqa: E731, E741
for _ in range(int(input())):
    a1, k = map(int, input().split())
    for _ in range(k - 1):
        d = list(map(int, str(a1)))
        maxi = max(d)
        mini = min(d)
        if mini == 0:
            break
        a1 += maxi * mini
    print(a1)
