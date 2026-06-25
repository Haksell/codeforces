# ruff: noqa: E731, E741
for _ in range(int(input())):
    a1, a2, *_, tot = map(int, input().split())
    print(a1, a2, tot - a1 - a2)
