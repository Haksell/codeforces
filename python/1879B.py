# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(min(n * min(a) + sum(b), n * min(b) + sum(a)))
