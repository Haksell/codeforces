# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    s = sum(a)
    for i, ai in enumerate(a):
        if s // (n - i) >= x:
            print(n - i)
            break
        s -= ai
    else:
        print(0)
