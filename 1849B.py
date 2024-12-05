# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [-ai % k for ai in a]
    print(*[i + 1 for i in sorted(range(n), key=a.__getitem__)])
