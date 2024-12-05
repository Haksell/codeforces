# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    l = sorted(
        [y - x for x, y in zip(map(int, input().split()), map(int, input().split()))]
    )
    i = 0
    j = n - 1
    res = 0
    while i < j:
        if l[i] + l[j] >= 0:
            res += 1
            j -= 1
        i += 1
    print(res)
