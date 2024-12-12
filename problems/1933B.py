# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = sum(a) % 3
    ms = {x % 3 for x in a}
    print(0 if m == 0 else 2 if m == 1 and 1 not in ms else 1)
