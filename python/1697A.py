# ruff: noqa: E731, E741
for _ in range(int(input())):
    _, e = map(int, input().split())
    a = list(map(int, input().split()))
    print(max(0, sum(a) - e))
