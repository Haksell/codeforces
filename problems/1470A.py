# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, m = map(int, input().split())
    k = [int(x) - 1 for x in input().split()]
    c = list(map(int, input().split()))
    print(sum(c[min(i, ki)] for i, ki in enumerate(sorted(k, reverse=True))))
