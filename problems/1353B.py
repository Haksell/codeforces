# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    for i in range(k):
        if b[~i] > a[i]:
            a[i], b[~i] = b[~i], a[i]
        else:
            break
    print(sum(a))
