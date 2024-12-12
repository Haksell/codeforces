# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    s = sum(x or 1 for x in a)
    print(a.count(0) + (s == 0))
