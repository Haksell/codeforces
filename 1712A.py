# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    print(sum(x > k for x in p[:k]))
